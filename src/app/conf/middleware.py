from app.conf.environ import env

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.middleware.real_ip.real_ip_middleware",
    "axes.middleware.AxesMiddleware",
]

if env("DEBUG", cast=bool, default=False):
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
