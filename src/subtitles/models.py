import datetime

from django.core import validators
from django.db import models

from subtitles import definitions


class Genre(models.Model):
    title = models.CharField(max_length=30)


class Film(models.Model):
    english_title = models.CharField(max_length=255)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    genres = models.ManyToManyField(Genre)
    released = models.PositiveIntegerField(
        blank=True,
        validators=[
            validators.MinValueValidator(1878),
            validators.MaxValueValidator(datetime.date.today().year + 1),
        ]
    )
    duration = models.DurationField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=30, choices=definitions.DIFFICULTY_CHOICES, blank=True)
    poster = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=1023, blank=True)
    idioms = models.JSONField(blank=True, null=True)
    difficult_phrases = models.JSONField(blank=True, null=True)
    uncommon_words = models.JSONField(blank=True, null=True)
    words_count = models.JSONField(blank=True, null=True)
    questions = models.JSONField(blank=True, null=True)