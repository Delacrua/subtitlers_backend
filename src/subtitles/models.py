from django.db import models

from subtitles import definitions


class Genre(models.Model):
    title = models.CharField(max_length=30)
    is_film_genre = models.BooleanField(default=False)
    is_series_genre = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=255)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    genres = models.ManyToManyField(Genre, related_name="films")
    released = models.PositiveIntegerField(blank=True)
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

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=255)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    genres = models.ManyToManyField(Genre, related_name="series")
    released = models.PositiveIntegerField(blank=True)
    ended = models.PositiveIntegerField(blank=True)
    number_of_seasons = models.PositiveIntegerField(blank=True)
    number_of_episodes = models.PositiveIntegerField(blank=True)
    difficulty_level = models.CharField(max_length=30, choices=definitions.DIFFICULTY_CHOICES, blank=True)
    poster = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    season_number = models.PositiveIntegerField(blank=True)
    series = models.ForeignKey(Series, related_name="seasons", on_delete=models.CASCADE)
    number_of_episodes = models.PositiveIntegerField(blank=True)
    released = models.PositiveIntegerField(blank=True)
    ended = models.PositiveIntegerField(blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.series} - season {self.season_number}"


class Episode(models.Model):
    season = models.ForeignKey(Season, related_name="episodes", on_delete=models.CASCADE)
    episode_number = models.PositiveIntegerField(blank=True)
    episode_title = models.CharField(max_length=255, blank=True)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    duration = models.DurationField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=1023, blank=True)
    idioms = models.JSONField(blank=True, null=True)
    difficult_phrases = models.JSONField(blank=True, null=True)
    uncommon_words = models.JSONField(blank=True, null=True)
    words_count = models.JSONField(blank=True, null=True)
    questions = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.season.series} - season {self.season.season_number} - episode {self.episode_number}"


class Word(models.Model):
    title = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    definition = models.CharField(max_length=255, null=True, blank=True)
    film = models.ManyToManyField(Film, related_name="words", null=True, blank=True)
    episode = models.ManyToManyField(Episode, related_name="words", null=True, blank=True)

    def __str__(self):
        return self.title


class Phrases(models.Model):
    title = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    definition = models.CharField(max_length=255, null=True, blank=True)
    film = models.ManyToManyField(Film, related_name="phrases", null=True, blank=True)
    episode = models.ManyToManyField(Episode, related_name="phrases", null=True, blank=True)
    is_idiom = models.BooleanField(default=False)

    def __str__(self):
        return self.title
