from django.core.management.base import BaseCommand

from subtitles import models as sbt_models
from subtitles.services.data.genres_list import BASE_GENRES_DATA


class Command(BaseCommand):
    """Django command for initial genres creation"""

    def handle(self, *args, **kwargs):
        """Entrypoint for command"""

        if sbt_models.Genre.objects.count() < len(BASE_GENRES_DATA):
            self.stdout.write("Base genres not found. Updating or creating base genres")
            for genre in BASE_GENRES_DATA:
                sbt_models.Genre.objects.update_or_create(
                    title=genre.get("title"),
                    defaults={
                        "readable": genre.get("readable"),
                        "is_film_genre": genre.get("is_film_genre"),
                        "is_series_genre": genre.get("is_series_genre"),
                    },
                )
        else:
            self.stdout.write("Base genres found, continue.")
