from rest_framework import viewsets

from subtitles import models as sbt_models
from subtitles.api import serializers as sbt_serializers

__all__ = [
    "FilmListViewSet",
    "EpisodeListViewSet",
]


class FilmListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Film.objects.all()
    serializer_class = sbt_serializers.FilmSerializer


class EpisodeListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Episode.objects.all()
    serializer_class = sbt_serializers.EpisodeSerializer
