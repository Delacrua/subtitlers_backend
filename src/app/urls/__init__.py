from django.contrib import admin
from django.urls import include
from django.urls import path

from app.conf.environ import env

api = [
    path("v1/", include("app.urls.v1", namespace="v1")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api)),
]

if env("DEBUG", cast=bool, default=False):
    import debug_toolbar  # type: ignore

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
