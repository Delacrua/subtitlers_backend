from rest_framework import serializers

from subtitles import models as sbt_models

__all__ = [
    "FilmSerializer",
]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.Genre
        fields = (
            "id",
            "title",
            "readable",
        )


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.Word
        exclude = (
            "film",
            "episode",
        )

    def serialize_quantity(self, word_instance) -> dict:  # type: ignore
        word_quantity_instance = word_instance.wordquantity_set.filter(film=self.context["film_instance"]).first()
        if word_quantity_instance:
            return WordQuantitySerializer(word_quantity_instance).data
        return {}

    def to_representation(self, instance) -> dict:  # type: ignore
        rep = super().to_representation(instance)
        return {**rep, **self.serialize_quantity(instance)}


class WordQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.WordQuantity
        fields = ("quantity",)


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.Phrase
        fields = (
            "text",
            "translations",
            "definition",
            "is_idiom",
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.Question
        fields = (
            "question_text",
            "q_translations",
            "answer_text",
            "a_translations",
        )


class FilmSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    words = serializers.SerializerMethodField()
    phrases = PhraseSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    def get_words(self, film):  # type: ignore
        return WordSerializer(film.words.all(), many=True, context={"film_instance": film}).data

    class Meta:
        model = sbt_models.Film
        fields = (
            "id",
            "title",
            "other_titles",
            "genres",
            "released",
            "duration",
            "difficulty_level",
            "poster",
            "description",
            "summary",
            "words",
            "phrases",
            "questions",
        )
