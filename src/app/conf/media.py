from app.conf.boilerplate import BASE_DIR
from app.conf.environ import env

MEDIA_URL = "/static/media/"
MEDIA_ROOT = BASE_DIR / env("MEDIA_ROOT", cast=str, default="vol/web/media")
