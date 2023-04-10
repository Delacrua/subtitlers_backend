from django.contrib import admin

from subtitles import models as sbt_models


class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ["genres"]


class SeriesAdmin(admin.ModelAdmin):
    filter_horizontal = ["genres"]


class PhraseAdmin(admin.ModelAdmin):
    filter_horizontal = ["film", "episode"]


admin.site.register(sbt_models.Genre)
admin.site.register(sbt_models.Word)
admin.site.register(sbt_models.Phrase, PhraseAdmin)
admin.site.register(sbt_models.FilmQuestion)
admin.site.register(sbt_models.EpisodeQuestion)
admin.site.register(sbt_models.Film, FilmAdmin)
admin.site.register(sbt_models.Series, SeriesAdmin)
admin.site.register(sbt_models.Season)
admin.site.register(sbt_models.Episode)
admin.site.register(sbt_models.EpisodeWordQuantity)
admin.site.register(sbt_models.FilmWordQuantity)
