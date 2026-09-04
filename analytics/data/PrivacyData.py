"""
Privacy notice content.

Deliberately English-only, unlike the rest of the interface. Machine-translating
a legal document produces text nobody can rely on and that the operator cannot
stand behind, so this states one authoritative version instead of seven
approximate ones.

Every factual claim here is checkable in this repository:
  - `analytics/models.py` is empty, so no upload can be persisted.
  - `analytics/views.py` reads the archive with `zipfile` in memory and renders
    the result; nothing is written to disk.
  - The only session key written is the language preference.
Change any of those and this file has to change with it.
"""

PRIVACY_UPDATED = "4 September 2026"
PRIVACY_UPDATED_ISO = "2026-09-04"

PRIVACY_DATA = {
    "header_title": "Privacy",
    "header_description": (
        "This tool reads a file you already own and shows you what is in it. "
        "Nothing you upload is stored — here is exactly what happens instead."
    ),
    "updated": PRIVACY_UPDATED,
    "updated_iso": PRIVACY_UPDATED_ISO,
    "meta_title": "Privacy — igstats",
    "meta_description": (
        "igstats stores nothing you upload. What happens to your Instagram "
        "export, the other people named in it, and your rights under Indonesian "
        "Law 27/2022."
    ),
    "sections": [
        {
            "id": "summary",
            "title": "The short version",
            "highlight": True,
            "paragraphs": [
                "Your export is read in memory, the result is rendered into the page you get back, and the request ends. There is no database record, no file on disk, and no copy kept anywhere.",
                "Refresh the page and the analysis is gone, because there was never anywhere for it to be kept. That is not a policy we apply by hand — the application defines no database models at all, so there is nothing for an upload to be written into.",
            ],
        },
        {
            "id": "who",
            "title": "Who operates this",
            "paragraphs": [
                "igstats is operated by PT RoneAI Teknologi Internasional, an Indonesian company trading as RoneAI, domiciled in Boyolali Regency, Central Java.",
                "It is an independent project. It is not affiliated with, endorsed by, or operated by Meta or Instagram, and it does not connect to any Instagram account. It only reads a file that you request and download from Instagram yourself.",
                "Indonesian Law No. 27 of 2022 on Personal Data Protection governs us, and this notice is written against it.",
            ],
        },
        {
            "id": "what",
            "title": "What we handle, and for how long",
            "paragraphs": [
                "Three things reach the server, and only one of them survives the request.",
            ],
            "table": {
                "head": ["What", "Why", "Kept"],
                "rows": [
                    [
                        "The followers and following files from your export, or the ZIP containing them",
                        "To compute mutuals, who does not follow you back, and who you do not follow back",
                        "Not kept. Parsed in memory, rendered into the response, discarded",
                    ],
                    [
                        "Your language preference",
                        "So the interface stays in the language you picked",
                        "A session cookie in your own browser",
                    ],
                    [
                        "Your IP address and browser, as any web server sees",
                        "Serving the request; abuse prevention by our host",
                        "In our host's standard request logs, under their retention",
                    ],
                ],
            },
            "after": [
                "We do not ask for, and cannot accept, your Instagram password. There is no login here and no connection to your account.",
            ],
        },
        {
            "id": "others",
            "title": "About the other people in your file",
            "highlight": True,
            "paragraphs": [
                "This deserves saying plainly, because most tools like this one skip it. Your export is a list of accounts, and those accounts belong to other people. Their usernames and the dates they followed you are their personal data, not only yours.",
                "So: their data is processed for the few seconds it takes to compute the answer you asked for, at your direction, and is then gone with everything else. We never store it, never build a profile from it, never contact anyone named in it, and never sell or share it. There is no advertising here and no analytics.",
                "What you do with the result afterwards is on you. Publishing a list of accounts that did not follow you back, or using it to pressure someone, is a use of other people's data that this tool cannot control and does not endorse.",
            ],
        },
        {
            "id": "basis",
            "title": "Why we are allowed to process it",
            "paragraphs": [
                "Under Article 20(2)(b) of the Personal Data Protection Act, we process what you upload to fulfil your own request — you asked for the analysis and it cannot be produced without the file.",
                "Server logs rest on Article 20(2)(f), our legitimate interest in keeping the service running and unabused.",
                "We do not rely on consent, so there is nothing here to withdraw. Since nothing is retained, there is also nothing to delete after the fact: closing the tab is the deletion.",
            ],
        },
        {
            "id": "processors",
            "title": "Who else is involved",
            "paragraphs": [
                "The application runs on Vercel, which serves every request and keeps its own standard request logs under its own privacy terms. Vercel is established outside Indonesia, so hosting the service involves a transfer out of the jurisdiction; we rely on Article 56(3) — binding contractual protection under the provider's published data processing terms — because Indonesia has not yet published a list of countries meeting the equivalent-protection test.",
                "Nobody else is involved. No analytics provider, no advertising network, no third-party font or asset host, and no external service receives your uploaded file.",
            ],
        },
        {
            "id": "rights",
            "title": "Your rights",
            "paragraphs": [
                "The Personal Data Protection Act gives you the right to information (Article 5), correction (Article 6), access and a copy (Article 7), erasure (Article 8), restriction (Article 11), compensation (Article 12), and portability (Article 13).",
                "Where a request needs action, the Act gives us 3 × 24 hours, not the thirty days people expect from European rules — Articles 30, 31, 40 and 41. In practice most requests about this tool have a very short answer, because we hold nothing about you to access, correct, or erase.",
                "Email hello@rone.dev. There is no charge and you will not be asked to justify the request. If our answer does not satisfy you, you can complain to the Ministry of Communication and Digital Affairs, which supervises data protection until Lembaga PDP is established.",
            ],
        },
        {
            "id": "security",
            "title": "Security, and its limits",
            "paragraphs": [
                "Everything is served over HTTPS. Uploaded archives are opened in memory and never written to disk, and the strongest measure here is structural: with no data store, there is no store to breach.",
                "The honest limit is that an upload does travel over the network and passes through our host's infrastructure while the request is in flight. Encryption in transit protects it there; nothing can make a file you send to a server never have left your machine.",
                "If you find a vulnerability, email founder@rone.dev rather than opening a public issue. Scope and safe-harbour terms are at https://rone.dev/security.",
            ],
        },
        {
            "id": "children",
            "title": "Children",
            "paragraphs": [
                "This tool is not directed at children, and we do not knowingly process data from anyone under 18. If you believe a child has used it, tell us.",
            ],
        },
        {
            "id": "changes",
            "title": "Changes",
            "paragraphs": [
                "If the tool starts doing something different, this page changes with it and the date at the top moves. If we ever added storage of any kind, that would be the change this page led with.",
            ],
        },
    ],
    "contact_title": "Contact",
    "contact_lines": [
        "PT RoneAI Teknologi Internasional (RoneAI)",
        "Boyolali Regency, Central Java, Indonesia",
        "General and data protection: hello@rone.dev",
        "Security reports: founder@rone.dev",
    ],
}


def get_privacy_data():
    """Privacy page content. Not language-switched — see the module docstring."""
    return PRIVACY_DATA
