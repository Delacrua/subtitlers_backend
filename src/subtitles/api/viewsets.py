from rest_framework import viewsets

from django.db.models.query import QuerySet

from subtitles import models as sbt_models
from subtitles.api import serializers as sbt_serializers

__all__ = [
    "FilmViewSet",
    "SeriesViewSet",
    "SeasonViewSet",
    "EpisodeViewSet",
]


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Film.objects.prefetch_related(
        "words",
        "genres",
        "phrases",
        "questions",
    ).all()
    serializer_class = sbt_serializers.FilmSerializer


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Series.objects.prefetch_related(
        "seasons",
        "genres",
        "seasons__episodes",
    ).all()
    serializer_class = sbt_serializers.SeriesSerializer


class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Season.objects.all()
    serializer_class = sbt_serializers.SeasonSeralizer

    def get_queryset(self) -> "QuerySet[sbt_models.Season]":
        return sbt_models.Season.objects.filter(series=self.kwargs["series_pk"])


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Episode.objects.all()
    serializer_class = sbt_serializers.EpisodeSerializer

    def get_queryset(self) -> "QuerySet[sbt_models.Episode]":
        return sbt_models.Episode.objects.filter(season=self.kwargs["season_pk"])
