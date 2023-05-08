from dataclasses import dataclass

from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import OpenApiResponse

from subtitles.api import serializers as sbt_serializers


@dataclass
class SwaggerResponse:
    """a dataclass for storing responses schemas for Swagger purposes"""

    genres_difficulties_response = {
        200: OpenApiResponse(
            response=sbt_serializers.GenreSerializer,
            examples=[
                OpenApiExample(
                    "Info endpoint example",
                    description="An example of response info endpoint",
                    value={
                        "genres": [
                            {"id": 34, "title": "action", "readable": "Action"},
                            {"id": 47, "title": "action_comedy", "readable": "Action-comedy"},
                        ],
                        "difficultyLevels": [
                            {"title": "beginner", "readable": "Beginner"},
                            {"title": "beginner_intermediate", "readable": "Beginner - Intermediate"},
                        ],
                    },
                    response_only=True,
                ),
            ],
        ),
    }
