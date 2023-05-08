from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models.query import QuerySet

from subtitles import models as sbt_models
from subtitles.api import responses as sbt_responses
from subtitles.api import serializers as sbt_serializers
from subtitles.definitions import DIFFICULTY_CHOICES

__all__ = [
    "FilmViewSet",
    "SeriesViewSet",
    "SeasonViewSet",
    "EpisodeViewSet",
    "GenresDifficultyLevelsView",
]


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = sbt_models.Film.objects.prefetch_related(
        "words",
        "genres",
        "phrases",
        "questions",
    ).all()
    serializer_class = sbt_serializers.FilmSerializer
    filterset_fields = ("difficulty_level", "genres")


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


class GenresDifficultyLevelsView(APIView):
    @extend_schema(responses=sbt_responses.SwaggerResponse.genres_difficulties_response)
    def get(self, request: Request) -> Response:
        genres = sbt_models.Genre.objects.all()
        genres_serializer = sbt_serializers.GenreSerializer(genres, many=True)
        difficulty_levels = [{"title": level[0], "readable": level[1]} for level in DIFFICULTY_CHOICES]
        data = {
            "genres": genres_serializer.data,
            "difficulty_levels": difficulty_levels,
        }

        return Response(data)
