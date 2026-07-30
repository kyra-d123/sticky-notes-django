"""Configure Django Admin for the notes application."""

from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Configure how notes are displayed in Django Admin."""

    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "content")
    ordering = ("-updated_at",)
