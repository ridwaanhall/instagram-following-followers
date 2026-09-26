"""
Pure functions that turn an Instagram data export into the numbers the results
page shows. No Django imports, so they are trivial to test.
"""

from datetime import datetime
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

    cutoff = (now or datetime.now().timestamp()) - THIRTY_DAYS
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
    }
