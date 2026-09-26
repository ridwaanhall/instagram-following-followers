"""
Terms of use content.

English-only for the same reason as the privacy notice: one authoritative
version rather than seven machine translations of a legal text. Rendered by
the shared analytics/legal.html template, so the shape matches PrivacyData.
"""

TERMS_UPDATED = "27 September 2026"
TERMS_UPDATED_ISO = "2026-09-27"

TERMS_DATA = {
    "header_title": "Terms",
    "header_description": (
        "The rules for using igstats, kept short. It is a free tool that reads "
        "a file you already own; these terms say what you can expect from it "
        "and what it expects from you."
    ),
    "updated": TERMS_UPDATED,
    "updated_iso": TERMS_UPDATED_ISO,
    "meta_title": "Terms — igstats",
    "meta_description": (
        "Terms of use for igstats, the free Instagram followers and following "
        "analyzer by RoneAI: acceptable use, no warranty, and governing law."
    ),
    "sections": [
        {
            "id": "summary",
            "title": "The short version",
            "highlight": True,
            "paragraphs": [
                "Use igstats to read your own Instagram export. Do not use it, or its results, to harass anyone. It is free, it comes with no guarantees, and we can change or stop it at any time.",
            ],
        },
        {
            "id": "service",
            "title": "What igstats is",
            "paragraphs": [
                "igstats is operated by PT RoneAI Teknologi Internasional (RoneAI), a company in Indonesia. It compares the followers and following lists in an Instagram data export you upload and shows the differences.",
                "It is not affiliated with, endorsed by, or connected to Meta or Instagram. It never asks for your Instagram password and never connects to your account. Instagram is a trademark of its owner and is named here only to describe what the tool reads.",
            ],
        },
        {
            "id": "use",
            "title": "Acceptable use",
            "paragraphs": [
                "Only upload an export of an account you own or are authorised to manage.",
                "Your export names other people. Do not publish the lists, use them to pressure or shame anyone, or combine them with other data to profile people.",
                "Do not attempt to disrupt the service, overload it with automated requests, probe it for vulnerabilities outside the process in our privacy notice, or use it for anything unlawful.",
            ],
        },
        {
            "id": "data",
            "title": "Your data",
            "paragraphs": [
                "Uploads are read in memory to produce your report and are not stored. The privacy notice explains exactly what reaches the server and for how long, and it forms part of these terms.",
            ],
        },
        {
            "id": "warranty",
            "title": "No warranty",
            "paragraphs": [
                "igstats is provided free and as is. Instagram can change its export format at any time, so results may be incomplete or wrong. Check anything important on Instagram itself before acting on it.",
                "We do not promise the service will be available, uninterrupted, or error-free.",
            ],
        },
        {
            "id": "liability",
            "title": "Limitation of liability",
            "paragraphs": [
                "To the extent the law allows, RoneAI is not liable for indirect or consequential loss arising from use of igstats, including decisions you make about who to follow or unfollow. Nothing in these terms limits liability that cannot be limited under Indonesian law.",
            ],
        },
        {
            "id": "ip",
            "title": "Source code and names",
            "paragraphs": [
                "The igstats source code is published under the MIT License on GitHub. The igstats and RoneAI names are not covered by that licence.",
            ],
        },
        {
            "id": "law",
            "title": "Governing law",
            "paragraphs": [
                "These terms are governed by the laws of the Republic of Indonesia.",
            ],
        },
        {
            "id": "changes",
            "title": "Changes",
            "paragraphs": [
                "We may update these terms. The date at the top changes when we do, and continuing to use igstats after that means you accept the new version.",
            ],
        },
    ],
    "contact_title": "Contact",
    "contact_lines": [
        "RoneAI",
        "Indonesia",
        "hello@rone.dev",
    ],
}
