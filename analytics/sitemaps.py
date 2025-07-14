from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return [
            'home',
            'upload_file', 
            'zip_upload',
            'text_input',
            'tutorial'
        ]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        from datetime import datetime
        return datetime(2025, 7, 14, 22, 55)

    def priority(self, item):
        return 1.0 if item == 'home' else 0.8

sitemaps = {
    'static': StaticViewSitemap,
}
