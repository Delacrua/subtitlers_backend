from app.conf.environ import env

MEDIA_URL = "/static/media/"
MEDIA_ROOT = env("MEDIA_ROOT", cast=str, default="vol/web/media")
