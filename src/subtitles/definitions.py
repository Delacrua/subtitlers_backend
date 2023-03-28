from django.utils.translation import gettext_lazy as _

GENRE_CHOICES = (  # TO DO
    ("action", _("Action")),
    ("adventure", _("Adventure")),
    ("comedy", _("Comedy")),
    ("crime_mystery", _("Crime and mystery")),
    ("fantasy", _("Fantasy")),
    ("historical", _("Historical")),
    ("historical_fiction", _("Historical fiction")),
    ("horror", _("Horror")),
    ("romance", _("Romance")),
    ("satire", _("Satire")),
    ("science_fiction", _("Science fiction")),
    ("cyberpunk", _("Cyberpunk and derivatives")),
    ("speculative", _("Speculative")),
    ("thriller", _("Thriller")),
    ("isekai", _("Isekai")),
    ("other", _("Other")),
)

DIFFICULTY_CHOICES = (
    ("beginner", _("Beginners")),
    ("beginner_intermediate", _("Beginner - Intermediate")),
    ("intermediate", _("Intermediate")),
    ("intermediate_advanced", _("Intermediate - Advanced")),
    ("advanced", _("Advanced")),
)
