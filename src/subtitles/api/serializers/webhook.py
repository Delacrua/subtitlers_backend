from rest_framework import serializers

__all__ = [
    "WordWebhookSerializer",
    "PhraseWebhookSerializer",
    "QuestionWebhookSerializer",
    "FilmWebhookSerializer",
    "FilmEventWebhookSerializer",
]


class WordWebhookSerializer(serializers.Serializer):
    text = serializers.CharField()
    translations = serializers.JSONField(allow_null=True)
    definition = serializers.CharField(allow_blank=True, allow_null=True)
    is_uncommon = serializers.BooleanField(default=False)
    quantity = serializers.IntegerField(default=0)


class PhraseWebhookSerializer(serializers.Serializer):
    text = serializers.CharField()
    translations = serializers.JSONField(allow_null=True)
    definition = serializers.CharField(allow_blank=True, allow_null=True)
    is_idiom = serializers.BooleanField(default=False)


class QuestionWebhookSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    question_translations = serializers.JSONField(allow_null=True)
    answer_text = serializers.CharField(allow_blank=True, allow_null=True)
    answer_translations = serializers.JSONField(allow_null=True)


class FilmWebhookSerializer(serializers.Serializer):
    title = serializers.CharField()
    other_titles = serializers.JSONField(allow_null=True)
    released = serializers.IntegerField(allow_null=True)
    duration = serializers.DurationField(allow_null=True)
    genres = serializers.ListField(allow_null=True)
    difficulty_level = serializers.CharField(allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    summary = serializers.CharField(allow_blank=True, allow_null=True)
    words = WordWebhookSerializer(many=True, allow_null=True, allow_empty=True)
    phrases = PhraseWebhookSerializer(many=True, allow_null=True, allow_empty=True)
    questions = QuestionWebhookSerializer(many=True, allow_null=True, allow_empty=True)


class FilmEventWebhookSerializer(serializers.Serializer):
    event = serializers.CharField()
    film_data = FilmWebhookSerializer(many=False)

