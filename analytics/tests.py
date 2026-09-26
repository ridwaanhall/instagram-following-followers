import io
import json
import zipfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .analysis import analyze, extract_username, username_from_href

FOLLOWING = {
    "relationships_following": [
        {"title": "alice", "string_list_data": [{"href": "https://www.instagram.com/_u/alice", "timestamp": 1700000000}]},
        {"title": "", "string_list_data": [{"href": "https://www.instagram.com/bob", "value": "bob", "timestamp": 1700000100}]},
        {"title": "", "string_list_data": [{"href": "https://www.instagram.com/_u/carol", "timestamp": 1700000200}]},
    ]
}
FOLLOWERS = [
    {"title": "", "string_list_data": [{"href": "https://www.instagram.com/alice", "value": "alice", "timestamp": 1700000300}]},
    {"title": "", "string_list_data": [{"href": "https://www.instagram.com/dave", "value": "dave", "timestamp": 1700000400}]},
]


class UsernameParsingTests(TestCase):
    def test_accepts_instagram_profile_urls(self):
        self.assertEqual(username_from_href("https://www.instagram.com/alice"), "alice")
        self.assertEqual(username_from_href("https://instagram.com/_u/bob/"), "bob")
        self.assertEqual(username_from_href("http://m.instagram.com/carol?x=1"), "carol")

    def test_rejects_lookalike_hosts(self):
        # The CodeQL "incomplete URL substring sanitization" cases.
        self.assertIsNone(username_from_href("https://evil.com/instagram.com/alice"))
        self.assertIsNone(username_from_href("https://instagram.com.evil.com/alice"))
        self.assertIsNone(username_from_href("https://evil.com/_u/alice"))
        self.assertIsNone(username_from_href("javascript:alert(1)//instagram.com/x"))

    def test_value_then_title_then_href(self):
        self.assertEqual(extract_username({"value": "v", "href": "https://instagram.com/h"}, {"title": "t"}), "v")
        self.assertEqual(extract_username({"href": "https://instagram.com/h"}, {"title": "t"}), "t")
        self.assertEqual(extract_username({"href": "https://instagram.com/h"}, {"title": ""}), "h")


class AnalyzeTests(TestCase):
    def test_counts_and_lists(self):
        result = analyze(FOLLOWING, FOLLOWERS, now=1700000500)
        self.assertEqual(result["count_following_count"], 3)
        self.assertEqual(result["count_followers_count"], 2)
        self.assertEqual(result["count_mutual_follow"], 1)
        self.assertEqual([r["username"] for r in result["list_non_follow_back"]], ["carol", "bob"])
        self.assertEqual([r["username"] for r in result["list_not_following_back"]], ["dave"])
        self.assertEqual(result["mutual_rate"], 33.3)
        self.assertEqual(result["follow_back_rate"], 50.0)
        self.assertEqual(result["recent_follows_count"], 3)

    def test_empty_input(self):
        result = analyze({}, [])
        self.assertEqual(result["count_following_count"], 0)
        self.assertEqual(result["follow_ratio"], 0)


def make_zip(files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, data in files.items():
            z.writestr(name, json.dumps(data))
    return SimpleUploadedFile("export.zip", buf.getvalue(), content_type="application/zip")


class ViewTests(TestCase):
    def test_pages_render(self):
        for url in ["/", "/zip/", "/upload/", "/text/", "/tutorial/", "/privacy/", "/terms/", "/sitemap.xml", "/robots.txt", "/.well-known/security.txt"]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_seo_and_security_basics(self):
        response = self.client.get("/")
        csp = response["Content-Security-Policy"]
        self.assertIn("default-src 'self'", csp)
        self.assertIn("'nonce-", csp)
        self.assertContains(response, 'rel="canonical"')
        self.assertContains(response, "og-image.png")
        self.assertContains(response, "https://rone.dev")
        sitemap = self.client.get("/sitemap.xml").content.decode()
        self.assertIn("/terms/", sitemap)
        self.assertIn("mailto:", self.client.get("/.well-known/security.txt").content.decode())

    def test_custom_404(self):
        response = self.client.get("/definitely-missing/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page not found", status_code=404)

    def test_zip_upload(self):
        upload = make_zip({
            "connections/followers_and_following/following.json": FOLLOWING,
            "connections/followers_and_following/followers_1.json": FOLLOWERS,
        })
        response = self.client.post("/zip/", {"zip_file": upload})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "analytics/results.html")
        self.assertContains(response, "instagram.com/carol")

    def test_zip_missing_file(self):
        response = self.client.post("/zip/", {"zip_file": make_zip({"following.json": FOLLOWING})})
        self.assertTemplateUsed(response, "analytics/zip_upload.html")
        self.assertContains(response, "followers_1.json")

    def test_bad_zip(self):
        upload = SimpleUploadedFile("export.zip", b"not a zip")
        response = self.client.post("/zip/", {"zip_file": upload})
        self.assertContains(response, "Invalid ZIP file format.")

    def test_file_upload(self):
        response = self.client.post("/upload/", {
            "following_file": SimpleUploadedFile("following.json", json.dumps(FOLLOWING).encode()),
            "followers_file": SimpleUploadedFile("followers_1.json", json.dumps(FOLLOWERS).encode()),
        })
        self.assertTemplateUsed(response, "analytics/results.html")

    def test_text_input_invalid_json(self):
        response = self.client.post("/text/", {"following_text": "{bad", "followers_text": "[]"})
        self.assertTemplateUsed(response, "analytics/text_input.html")
        self.assertContains(response, "Invalid JSON input format.")

    def test_text_input(self):
        response = self.client.post("/text/", {
            "following_text": json.dumps(FOLLOWING),
            "followers_text": json.dumps(FOLLOWERS),
        })
        self.assertTemplateUsed(response, "analytics/results.html")
        self.assertContains(response, "instagram.com/dave")


class LanguageSwitchTests(TestCase):
    def test_switch_and_safe_redirect(self):
        response = self.client.get("/set-language/?lang=id&next=/privacy/")
        self.assertRedirects(response, "/privacy/", fetch_redirect_response=False)
        self.assertContains(self.client.get("/"), "Beranda")

    def test_rejects_offsite_next(self):
        # The CodeQL "URL redirection from remote source" cases.
        for target in ["https://evil.com/", "//evil.com", "https:///evil.com"]:
            with self.subTest(target=target):
                response = self.client.post("/set-language/", {"language": "en", "next": target})
                self.assertEqual(response["Location"], "/")
        response = self.client.get("/set-language/?lang=en", HTTP_REFERER="https://evil.com/")
        self.assertEqual(response["Location"], "/")
