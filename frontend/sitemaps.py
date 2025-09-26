from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    protocol = 'https'
    def items(self):
        return ['frontend:home', 'frontend:about', 'accounts:login']

    def location(self, item):
        return reverse(item)
