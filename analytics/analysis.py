"""
Pure functions that turn an Instagram data export into the numbers the results
page shows. No Django imports, so they are trivial to test.
"""

from datetime import date, datetime, timezone
from statistics import median
from urllib.parse import urlparse

INSTAGRAM_HOSTS = {"instagram.com", "www.instagram.com", "m.instagram.com"}
PROFILE_URL = "https://www.instagram.com/{}"
THIRTY_DAYS = 30 * 24 * 60 * 60


def username_from_href(href):
    """Return the username in an Instagram profile URL, or None.

    Handles both ``instagram.com/<name>`` and ``instagram.com/_u/<name>``. The
    host is compared exactly, so ``evil.com/instagram.com/x`` is rejected.
    """
    try:
        parsed = urlparse(href)
    except (TypeError, ValueError):
        return None
    if parsed.scheme not in ("http", "https") or (parsed.hostname or "").lower() not in INSTAGRAM_HOSTS:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if parts and parts[0] == "_u":
        parts = parts[1:]
    return parts[0] if parts else None


def extract_username(user, item):
    """Username for one ``string_list_data`` entry.

    Old exports put it in ``value``; newer ones leave ``value`` out and put it
    in the parent item's ``title``; the profile ``href`` is the last resort.
    """
    if user.get("value"):
        return user["value"]
    if item.get("title"):
        return item["title"]
    if user.get("href"):
        return username_from_href(user["href"])
    return None


def extract_users(items):
    """Map username -> timestamp (or None) for a list of export items."""
    users = {}
    for item in items:
        for user in item.get("string_list_data", []):
            username = extract_username(user, item)
            if username:
                users[username] = user.get("timestamp")
    return users


def following_items(data):
    """``following.json`` is an object; tolerate a bare list too."""
    if isinstance(data, dict):
        return data.get("relationships_following", [])
    return data


def followers_items(data):
    """``followers_1.json`` is a list; tolerate the object form too."""
    if isinstance(data, dict):
        return data.get("relationships_followers", [])
    return data


def format_date(timestamp):
    if not timestamp:
        return None
    return datetime.fromtimestamp(timestamp).strftime("%b %d, %Y")


def _row(username, followed=None, follower=None):
    return {
        "username": username,
        "href": PROFILE_URL.format(username),
        "followed_timestamp": followed,
        "followed_date": format_date(followed),
        "follower_timestamp": follower,
        "follower_date": format_date(follower),
    }


def _month(ts):
    d = datetime.fromtimestamp(ts, tz=timezone.utc)
    return (d.year, d.month)


def insights(following, followers, now):
    """Timeline and mutual-origin figures for the results dashboard.

    `following` and `followers` map username -> timestamp (or None).
    """
    now_dt = datetime.fromtimestamp(now, tz=timezone.utc)
    months = []
    y, m = now_dt.year, now_dt.month
    for _ in range(12):
        months.append((y, m))
        y, m = (y, m - 1) if m > 1 else (y - 1, 12)
    months.reverse()

    def per_month(users):
        counts = {}
        for ts in users.values():
            if ts:
                counts[_month(ts)] = counts.get(_month(ts), 0) + 1
        return counts

    f_counts, r_counts = per_month(following), per_month(followers)
    peak = max([f_counts.get(k, 0) for k in months] + [r_counts.get(k, 0) for k in months] + [0])
    timeline = [
        {
            "month": date(yy, mm, 1),
            "following": f_counts.get((yy, mm), 0),
            "followers": r_counts.get((yy, mm), 0),
            "h_following": round(f_counts.get((yy, mm), 0) / peak * 100, 1) if peak else 0,
            "h_followers": round(r_counts.get((yy, mm), 0) / peak * 100, 1) if peak else 0,
        }
        for yy, mm in months
    ]

    you_first = they_first = 0
    back_days = []
    for name in following.keys() & followers.keys():
        a, b = following[name], followers[name]
        if not (a and b):
            continue
        if a <= b:
            you_first += 1
            back_days.append((b - a) / 86400)
        else:
            they_first += 1
    dated = you_first + they_first

    all_ts = [t for t in [*following.values(), *followers.values()] if t]
    totals = {k: f_counts.get(k, 0) + r_counts.get(k, 0) for k in f_counts.keys() | r_counts.keys()}
    busiest = max(totals, key=totals.get) if totals else None

    return {
        "timeline": timeline,
        "timeline_peak": peak,
        "timeline_total_following": sum(t["following"] for t in timeline),
        "timeline_total_followers": sum(t["followers"] for t in timeline),
        "has_dates": bool(all_ts),
        "you_first": you_first,
        "they_first": they_first,
        "you_first_pct": round(you_first / dated * 100) if dated else 0,
        "they_first_pct": round(they_first / dated * 100) if dated else 0,
        "median_followback_days": round(median(back_days)) if back_days else None,
        "first_connection": datetime.fromtimestamp(min(all_ts), tz=timezone.utc).date() if all_ts else None,
        "busiest_month": date(busiest[0], busiest[1], 1) if busiest else None,
        "busiest_month_count": totals[busiest] if busiest else 0,
    }


def analyze(following_data, followers_data, now=None):
    """Compute counts, lists and ratios for the results page."""
    following = extract_users(following_items(following_data))
    followers = extract_users(followers_items(followers_data))
    following_set, followers_set = set(following), set(followers)
    mutual_set = following_set & followers_set

    mutual = [_row(u, following[u], followers[u]) for u in mutual_set]
    non_follow_back = [_row(u, followed=following[u]) for u in following_set - followers_set]
    not_following_back = [_row(u, follower=followers[u]) for u in followers_set - following_set]

    mutual.sort(key=lambda r: r["followed_timestamp"] or 0, reverse=True)
    non_follow_back.sort(key=lambda r: r["followed_timestamp"] or 0, reverse=True)
    not_following_back.sort(key=lambda r: r["follower_timestamp"] or 0, reverse=True)

    now = now or datetime.now().timestamp()
    cutoff = now - THIRTY_DAYS
    following_count, followers_count, mutual_count = len(following_set), len(followers_set), len(mutual_set)

    return {
        "count_following_count": following_count,
        "count_followers_count": followers_count,
        "count_mutual_follow": mutual_count,
        "count_non_follow_back": len(non_follow_back),
        "count_not_following_back": len(not_following_back),
        "list_mutual_follow": mutual,
        "list_non_follow_back": non_follow_back,
        "list_not_following_back": not_following_back,
        "recent_follows_count": sum(1 for t in following.values() if t and t > cutoff),
        "recent_followers_count": sum(1 for t in followers.values() if t and t > cutoff),
        "mutual_rate": round(mutual_count / following_count * 100, 1) if following_count else 0,
        "follow_back_rate": round(mutual_count / followers_count * 100, 1) if followers_count else 0,
        "follow_ratio": round(followers_count / following_count, 2) if following_count else 0,
        **insights(following, followers, now),
    }
