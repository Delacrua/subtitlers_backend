# Application definition
from app.conf.environ import env

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

APPS = [
    "app",
    "a12n",
    "users",
    "subtitles",
]

THIRD_PARTY_APPS = [
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_jwt.blacklist",
    "django_filters",
    "axes",
    "corsheaders",
]

if env("DEBUG", cast=bool, default=False):
    THIRD_PARTY_APPS.append("debug_toolbar")

INSTALLED_APPS = DEFAULT_APPS + APPS + THIRD_PARTY_APPS
