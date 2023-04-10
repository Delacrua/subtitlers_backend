# Generated by Django 4.1.7 on 2023-04-07 14:27

from django.db import migrations
from django.db import models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("subtitles", "0004_episodewordquantity_delete_wordquantity_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EpisodeQuestion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question_text", models.CharField(max_length=255)),
                ("question_translations", models.JSONField(blank=True, null=True)),
                ("answer_text", models.CharField(max_length=255)),
                ("answer_translations", models.JSONField(blank=True, null=True)),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="subtitles.episode",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FilmQuestion",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question_text", models.CharField(max_length=255)),
                ("question_translations", models.JSONField(blank=True, null=True)),
                ("answer_text", models.CharField(max_length=255)),
                ("answer_translations", models.JSONField(blank=True, null=True)),
                (
                    "film",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="subtitles.film",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
