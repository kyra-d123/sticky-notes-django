"""Define database models for the notes application."""

from django.db import models


class Note(models.Model):
    """Represent a sticky note stored in the database."""

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define display ordering for Note objects."""

        ordering = ["-updated_at"]

    def __str__(self):
        """Return the note title as its string representation."""
        return self.title