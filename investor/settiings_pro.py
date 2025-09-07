import os

from .settings import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "yourdomain.com").split(",")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
