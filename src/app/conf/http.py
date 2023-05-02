from app.conf.environ import env

ALLOWED_HOSTS = ["*"]  # host validation is not necessary in 2020
CSRF_TRUSTED_ORIGINS: list = [
    "https://*.flerman.com",
]

CORS_ALLOW_ALL_ORIGINS = True

SITE_ID = env("SITE_ID", cast=int, default=2):

if env("DEBUG", cast=bool, default=False):
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
