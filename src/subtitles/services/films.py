from subtitles import models as sbt_models


class CreateFilmService:
    """A service for creation and updating of film instances"""

    def __init__(self, film_data: dict) -> None:
        """
        :param film_data: dictionary with film data
        """
        self.film_data = film_data

    def __call__(self) -> sbt_models.Film:
        return self.act()

    def act(self) -> sbt_models.Film:
        """
        :return: a sbt_models.Film object
        """
        print(self.film_data)
        film_object, created = self._update_or_create_film_object()

        words_data = self.film_data.get("words", {})
        if words_data:
            self._add_words_with_quantities_to_film(film_object)

        phrases_data = self.film_data.get("phrases", {})
        if phrases_data:
            self._add_phrases_to_film(film_object)

        questions_data = self.film_data.get("questions", {})
        if questions_data:
            self._add_questions_to_film(film_object)

        genres_data = self.film_data.get("genres", [])
        if genres_data:
            self._add_genres_to_film(film_object)

        return film_object

    def _update_or_create_film_object(self) -> tuple[sbt_models.Film, bool]:
        """
        a helper method for Film object updating or creating in database
        """
        return sbt_models.Film.objects.update_or_create(
            title=self.film_data.get("title"),
            defaults={
                "other_titles": self.film_data.get("other_titles"),
                "released": self.film_data.get("released"),
                "duration": self.film_data.get("duration"),
                "difficulty_level": self.film_data.get("difficulty_level"),
                "description": self.film_data.get("description"),
                "summary": self.film_data.get("summary"),
            },
        )

    @staticmethod
    def _get_or_create_word(word_data: dict) -> tuple[sbt_models.Word, bool]:
        return sbt_models.Word.objects.get_or_create(
            text=word_data.get("text"),
            defaults={
                "translations": word_data.get("translations", None),
                "definition": word_data.get("translations") if word_data.get("translations") else "",
                "is_uncommon": bool(word_data.get("is_uncommon")),
            },
        )

    def _add_words_with_quantities_to_film(self, film_object: sbt_models.Film) -> None:
        for word_data in self.film_data.get("words", {}):
            if word_data:
                word_object, created = self._get_or_create_word(word_data)
                film_word_quantity, created = sbt_models.FilmWordQuantity.objects.get_or_create(
                    word=word_object,
                    film=film_object,
                    defaults={
                        "quantity": word_data.get("quantity", 0),
                    },
                )

    def _add_phrases_to_film(self, film_object: sbt_models.Film) -> None:
        for phrase_data in self.film_data.get("phrases", {}):
            if phrase_data:
                phrase_object, created = sbt_models.Phrase.objects.get_or_create(
                    text=phrase_data.get("text"),
                    defaults={
                        "translations": phrase_data.get("translations", None),
                        "definition": phrase_data.get("definition") if phrase_data.get("definition") else "",
                        "is_idiom": bool(phrase_data.get("is_idiom")),
                    },
                )
                film_object.phrases.add(phrase_object)

    def _add_questions_to_film(self, film_object: sbt_models.Film) -> None:
        for question_data in self.film_data.get("questions", {}):
            if question_data:
                question_object, created = sbt_models.FilmQuestion.objects.get_or_create(
                    question_text=question_data.get("question_text"),
                    film=film_object,
                    defaults={
                        "question_translations": question_data.get("question_translations", None),
                        "answer_translations": question_data.get("answer_translations", None),
                        "answer_text": question_data.get("answer_text") if question_data.get("answer_text") else "",
                    },
                )

    def _add_genres_to_film(self, film_object: sbt_models.Film) -> None:
        for genre in self.film_data.get("genres", []):
            genre_object = sbt_models.Genre.objects.get(title=genre)
            film_object.genres.add(genre_object)
