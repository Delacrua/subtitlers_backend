from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from subtitles.api import viewsets

router = SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("films/", viewsets.FilmListView.as_view(), name="films"),
]
