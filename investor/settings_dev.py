from .settings import *


DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# settings_test.py
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',  # ultra fast
]

