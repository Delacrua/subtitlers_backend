from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from subtitles.api import viewsets

router = SimpleRouter()
router.register("films", viewsets.FilmListViewSet, basename="films")
router.register("episodes", viewsets.EpisodeListViewSet, basename="episodes")


urlpatterns = [
    path("", include(router.urls)),
]
