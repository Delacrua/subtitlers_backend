from django.db import models

from subtitles import definitions


class Genre(models.Model):
    title = models.CharField(max_length=30)
    readable = models.CharField(max_length=30)
    is_film_genre = models.BooleanField(default=False)
    is_series_genre = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.readable


class Film(models.Model):
    title = models.CharField(max_length=255)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    released = models.PositiveIntegerField(blank=True)
    duration = models.DurationField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=30, choices=definitions.DIFFICULTY_CHOICES, blank=True)
    poster = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=1023, blank=True)
    genres = models.ManyToManyField(Genre, related_name="films")

    def __str__(self) -> str:
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=255)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    released = models.PositiveIntegerField(blank=True)
    ended = models.PositiveIntegerField(blank=True)
    difficulty_level = models.CharField(max_length=30, choices=definitions.DIFFICULTY_CHOICES, blank=True)
    poster = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    genres = models.ManyToManyField(Genre, related_name="series")

    def __str__(self) -> str:
        return self.title


class Season(models.Model):
    series = models.ForeignKey(Series, related_name="seasons", on_delete=models.CASCADE)
    season_number = models.PositiveIntegerField(blank=True)
    released = models.PositiveIntegerField(blank=True)
    ended = models.PositiveIntegerField(blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.series} - season {self.season_number}"


class Episode(models.Model):
    season = models.ForeignKey(Season, related_name="episodes", on_delete=models.CASCADE)
    episode_number = models.PositiveIntegerField(blank=True)
    episode_title = models.CharField(max_length=255, blank=True)
    other_titles = models.JSONField(blank=True, null=True)  # to discuss
    duration = models.DurationField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=1023, blank=True)

    def __str__(self) -> str:
        return f"{self.season.series} - season {self.season.season_number} - episode {self.episode_number}"


class Word(models.Model):
    text = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    definition = models.CharField(max_length=25, blank=True)
    is_uncommon = models.BooleanField(default=False)
    film = models.ManyToManyField(Film, through="FilmWordQuantity", related_name="words", blank=True)
    episode = models.ManyToManyField(Episode, through="EpisodeWordQuantity", related_name="words", blank=True)

    def __str__(self) -> str:
        return self.text


class EpisodeWordQuantity(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.episode} - {self.word}"


class FilmWordQuantity(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.film} - {self.word}"


class Phrase(models.Model):
    text = models.CharField(max_length=255)
    translations = models.JSONField(null=True, blank=True)
    definition = models.CharField(max_length=255, blank=True)
    is_idiom = models.BooleanField(default=False)
    film = models.ManyToManyField(Film, related_name="phrases", blank=True)
    episode = models.ManyToManyField(Episode, related_name="phrases", blank=True)

    def __str__(self) -> str:
        return self.text


class FilmQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    question_translations = models.JSONField(null=True, blank=True)
    answer_text = models.CharField(max_length=255)
    answer_translations = models.JSONField(null=True, blank=True)
    film = models.ForeignKey(Film, related_name="questions", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.film} - {self.question_text}"


class EpisodeQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    question_translations = models.JSONField(null=True, blank=True)
    answer_text = models.CharField(max_length=255)
    answer_translations = models.JSONField(null=True, blank=True)
    episode = models.ForeignKey(Episode, related_name="questions", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.episode} - {self.question_text}"
