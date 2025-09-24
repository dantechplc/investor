import os

from .settings import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "cryptotradeglobe.com" "140.238.65.187" "www.cryptotradeglobe.com").split(",")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.zoho.com'
DEFAULT_FROM_EMAIL = 'CryptoTrade Globe<info@cryptotradeglobe.com>'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info@cryptotradeglobe.com'
EMAIL_HOST_PASSWORD = 'D@ntech1212'

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


CORS_ALLOWED_ORIGINS = [
    "https://cryptotradeglobe.com",
    "https://www.cryptotradeglobe.com",
]
CSRF_TRUSTED_ORIGINS = [
    "https://cryptotradeglobe.com",
    "https://www.cryptotradeglobe.com",
]
