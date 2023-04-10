from app.conf.environ import env

ALLOWED_HOSTS = ["*"]  # host validation is not necessary in 2020
CSRF_TRUSTED_ORIGINS: list = []

CORS_ORIGIN_REGEX_WHITELIST = [
    r".*localhost.*",
    r".*127.0.0.1.*",
    r".*192.168.*",
    # add other origins
]

if env("DEBUG"):
    ABSOLUTE_HOST = "http://localhost:3000"
else:
    ABSOLUTE_HOST = "https://your.app.com"

if env("DEBUG", cast=bool, default=False):
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
