from rest_framework import generics

from subtitles import models as sbt_models
from subtitles.api import serializers as sbt_serializers

__all__ = [
    "FilmListView",
]


class FilmListView(generics.ListAPIView):
    queryset = sbt_models.Film.objects.all()
    serializer_class = sbt_serializers.FilmSerializer
