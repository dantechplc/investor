from django.urls import path

from .views import *

app_name = 'frontend'

urlpatterns=[
    path('', HomeView, name='home'),
    path('markets', MarketView, name='markets'),
    path('about-us', AboutView, name='about'),
    path('contact', ContactView, name='contact'),
    path('customers', CustomerView, name='customer'),
    path('legal', LegalView, name='legal'),
]