"""
URL configuration for investor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from frontend.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include(("accounts.urls", "accounts"), namespace="accounts")),
    # include staff-only urls under a prefix
    path("boss/", include("accounts.boss_urls",)),

    path("transaction/", include(("transaction.urls", "transaction"), namespace="transaction")),
    path('', include('frontend.urls', namespace='frontend') ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemaps'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.index_title = "CTG Admin"
admin.site.site_header = "CTG"


handler404 = 'frontend.views.error_404_view'
handler500 = 'frontend.views.error_500_view'
handler403 = 'frontend.views.error_403_view'