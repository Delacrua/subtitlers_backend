from django.contrib import admin

from subtitles import models as sbt_models


class FilmAdmin(admin.ModelAdmin):
    filter_horizontal = ["genres"]


class SeriesAdmin(admin.ModelAdmin):
    filter_horizontal = ["genres"]


admin.site.register(sbt_models.Genre)
admin.site.register(sbt_models.Word)
admin.site.register(sbt_models.Phrase)
admin.site.register(sbt_models.Question)
admin.site.register(sbt_models.Film, FilmAdmin)
admin.site.register(sbt_models.Series, SeriesAdmin)
admin.site.register(sbt_models.Season)
admin.site.register(sbt_models.Episode)
admin.site.register(sbt_models.WordQuantity)
