from typing import Optional

from subtitles import models as sbt_models
from subtitles.services.data.genres_list import GENRES_DATA


class GenreBulkCreateUpdateService:
    """A service for creating and updating of Genre instances in database"""

    def __init__(self, genre_data_list: Optional[list[dict]]) -> None:
        """
        :param genre_data_list: list of dictionaries with Genre data
        """
        self.genre_data_list = genre_data_list if genre_data_list else GENRES_DATA

    def __call__(self) -> None:
        return self.act()

    def act(self) -> None:
        """
        :return: a sbt_models.Genre object
        """
        if not sbt_models.Genre.objects.exists():
            sbt_models.Genre.objects.bulk_create(
                [
                    sbt_models.Genre(  # type: ignore
                        title=genre_data.get("title"),
                        readable=genre_data.get("readable"),
                        is_film_genre=genre_data.get("is_film_genre"),
                        is_series_genre=genre_data.get("is_series_genre"),
                    )
                    for genre_data in self.genre_data_list
                ]
            )
        else:
            for genre_data in self.genre_data_list:
                sbt_models.Genre.objects.update_or_create(
                    title=genre_data.get("title"),
                    defaults={
                        "readable": genre_data.get("readable"),
                        "is_film_genre": genre_data.get("is_film_genre"),
                        "is_series_genre": genre_data.get("is_series_genre"),
                    },
                )
