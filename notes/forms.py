"""Provide forms for creating and updating notes."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Collect and validate information for a Note object."""

    class Meta:
        """Connect the form to the Note model and its editable fields."""

        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a note title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the note content",
                    "rows": 6,
                }
            ),
        }