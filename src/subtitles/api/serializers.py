from rest_framework import serializers

from subtitles import models as sbt_models

__all__ = [
    "FilmSerializer",
    "EpisodeSerializer",
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
        if "film_instance" in self.context:
            word_quantity_instance = word_instance.wordquantity_set.filter(film=self.context["film_instance"]).first()
            if word_quantity_instance:
                return WordQuantitySerializer(word_quantity_instance).data
        elif "episode_instance" in self.context:
            word_quantity_instance = word_instance.wordquantity_set.filter(
                episode=self.context["episode_instance"]
            ).first()
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
            "question_translations",
            "answer_text",
            "answer_translations",
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


class SeriesSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = sbt_models.Series
        fields = "__all__"


class SeasonSeralizer(serializers.ModelSerializer):
    series = SeriesSerializer(many=False)

    class Meta:
        model = sbt_models.Season
        fields = "__all__"


class EpisodeSerializer(serializers.ModelSerializer):
    season = SeasonSeralizer(many=False)
    words = serializers.SerializerMethodField()
    phrases = PhraseSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    def get_words(self, episode):  # type: ignore
        return WordSerializer(episode.words.all(), many=True, context={"episode_instance": episode}).data

    class Meta:
        model = sbt_models.Episode
        fields = "__all__"
