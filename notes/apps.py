"""Configure the notes Django application."""

from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Configure application settings for the notes app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"