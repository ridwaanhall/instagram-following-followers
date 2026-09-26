from datetime import date

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .data.PrivacyData import PRIVACY_UPDATED_ISO
from .data.TermsData import TERMS_UPDATED_ISO

SITE_UPDATED = date(2026, 9, 27)


class StaticViewSitemap(Sitemap):
    """Every public page. Results are POST-only and never listed."""
    changefreq = 'monthly'
    protocol = 'https'

    pages = {
        'home': (1.0, SITE_UPDATED),
        'zip_upload': (0.9, SITE_UPDATED),
        'upload_file': (0.7, SITE_UPDATED),
        'text_input': (0.7, SITE_UPDATED),
        'tutorial': (0.8, SITE_UPDATED),
        'privacy': (0.3, date.fromisoformat(PRIVACY_UPDATED_ISO)),
        'terms': (0.3, date.fromisoformat(TERMS_UPDATED_ISO)),
    }

    def items(self):
        return list(self.pages)

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.pages[item][0]

    def lastmod(self, item):
        return self.pages[item][1]


sitemaps = {'static': StaticViewSitemap}
