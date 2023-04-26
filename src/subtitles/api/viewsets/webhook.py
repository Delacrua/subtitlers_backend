from typing import Any

from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from subtitles import models as sbt_models
from subtitles.api import serializers as sbt_serializers
from subtitles.services import CreateFilmService


class FilmEventWebhookView(generics.CreateAPIView):
    queryset = sbt_models.Film.objects.prefetch_related(
        "words",
        "genres",
        "phrases",
        "questions",
    ).all()
    serializer_class = sbt_serializers.FilmEventWebhookSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        if serializer.validated_data.get("event") == "film.created":
            film_data = serializer.validated_data.get("film_data")
            film_object = CreateFilmService(film_data)()
            return Response(
                status=status.HTTP_201_CREATED,
                data=sbt_serializers.FilmSerializer(film_object).data
            )
        return Response(data={"detail": "NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

