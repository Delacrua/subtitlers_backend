# Generated by Django 4.1.7 on 2023-04-06 09:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("subtitles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="season",
            name="number_of_episodes",
        ),
        migrations.RemoveField(
            model_name="series",
            name="number_of_episodes",
        ),
        migrations.RemoveField(
            model_name="series",
            name="number_of_seasons",
        ),
    ]
