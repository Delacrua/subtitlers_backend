from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers  # type: ignore

from django.urls import include
from django.urls import path

from subtitles.api import viewsets as sbt_views

film_router, series_router = SimpleRouter(), SimpleRouter()

film_router.register(
    "films",
    sbt_views.FilmViewSet,
    basename="films",
)

series_router.register(
    "series",
    sbt_views.SeriesViewSet,
    basename="series",
)

seasons_subrouter = routers.NestedSimpleRouter(
    series_router,
    "series",
    lookup="series",
)

seasons_subrouter.register(
    "seasons",
    sbt_views.SeasonViewSet,
    basename="seasons",
)

episodes_subrouter = routers.NestedSimpleRouter(
    seasons_subrouter,
    "seasons",
    lookup="season",
)

episodes_subrouter.register(
    "episodes",
    sbt_views.EpisodeViewSet,
    basename="episodes",
)

urlpatterns = [
    path("", include(film_router.urls)),
    path("", include(series_router.urls)),
    path("", include(seasons_subrouter.urls)),
    path("", include(episodes_subrouter.urls)),
    path("film_webhook/", sbt_views.FilmEventWebhookView.as_view(), name="film-webhook"),
    path("info/", sbt_views.GenresDifficultyLevelsView.as_view(), name="info"),
]
