from django.contrib.sites.models import Site
from rest_framework import serializers

from subtitles import models as sbt_models

__all__ = [
    "FilmSerializer",
    "EpisodeSerializer",
    "SeasonSeralizer",
    "SeriesSerializer",
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
            word_quantity_instance = word_instance.filmwordquantity_set.filter(
                film=self.context["film_instance"]
            ).first()
            if word_quantity_instance:
                return FilmWordQuantitySerializer(word_quantity_instance).data
        elif "episode_instance" in self.context:
            word_quantity_instance = word_instance.episodewordquantity_set.filter(
                episode=self.context["episode_instance"]
            ).first()
            if word_quantity_instance:
                return EpisodeWordQuantitySerializer(word_quantity_instance).data
        return {}

    def to_representation(self, instance) -> dict:  # type: ignore
        rep = super().to_representation(instance)
        return {**rep, **self.serialize_quantity(instance)}


class EpisodeWordQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.EpisodeWordQuantity
        fields = ("quantity",)


class FilmWordQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.FilmWordQuantity
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


class FilmQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.FilmQuestion
        fields = (
            "question_text",
            "question_translations",
            "answer_text",
            "answer_translations",
        )


class EpisodeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sbt_models.EpisodeQuestion
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
    questions = FilmQuestionSerializer(many=True, read_only=True)
    poster = serializers.SerializerMethodField()

    def get_words(self, film):  # type: ignore
        return WordSerializer(film.words.all(), many=True, context={"film_instance": film}).data

    def get_poster(self, film):  # type: ignore
        url_string = "%s%s" % (Site.objects.get_current().domain, film.poster.url)
        return "https://" + url_string.replace("//", "/")

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
    number_of_seasons = serializers.SerializerMethodField()
    number_of_episodes = serializers.SerializerMethodField()
    seasons = serializers.SerializerMethodField()

    def get_number_of_seasons(self, series):  # type: ignore
        return series.seasons.count()

    def get_seasons(self, series):  # type: ignore
        seasons_list = []
        for season in series.seasons.all():
            seasons_list.append({"id": season.id, "season_number": season.season_number})
        return seasons_list

    def get_number_of_episodes(self, series):  # type: ignore
        number_of_episodes = 0
        for season in series.seasons.all():
            number_of_episodes += season.episodes.count()
        return number_of_episodes

    class Meta:
        model = sbt_models.Series
        fields = (
            "id",
            "title",
            "other_titles",
            "released",
            "ended",
            "number_of_episodes",
            "difficulty_level",
            "poster",
            "description",
            "number_of_seasons",
            "seasons",
            "genres",
        )


class SeasonSeralizer(serializers.ModelSerializer):
    series = serializers.SerializerMethodField()
    episodes = serializers.SerializerMethodField()
    number_of_episodes = serializers.SerializerMethodField()

    def get_number_of_episodes(self, season):  # type: ignore
        return season.episodes.count()

    def get_episodes(self, season):  # type: ignore
        seasons_list = []
        for episode in season.episodes.all():
            seasons_list.append({"id": episode.id, "episode_number": episode.episode_number})
        return seasons_list

    def get_series(self, season):  # type: ignore
        return {"id": season.series.id, "title": season.series.title}

    class Meta:
        model = sbt_models.Season
        fields = (
            "id",
            "season_number",
            "released",
            "ended",
            "description",
            "number_of_episodes",
            "episodes",
            "series",
        )


class EpisodeSerializer(serializers.ModelSerializer):
    season = serializers.SerializerMethodField()
    words = serializers.SerializerMethodField()
    phrases = PhraseSerializer(many=True, read_only=True)
    questions = EpisodeQuestionSerializer(many=True, read_only=True)

    def get_words(self, episode):  # type: ignore
        return WordSerializer(episode.words.all(), many=True, context={"episode_instance": episode}).data

    def get_season(self, episode):  # type: ignore
        return {"id": episode.season.id, "title": str(episode.season)}

    class Meta:
        model = sbt_models.Episode
        fields = (
            "id",
            "episode_number",
            "episode_title",
            "other_titles",
            "duration",
            "description",
            "summary",
            "words",
            "phrases",
            "questions",
            "season",
        )
