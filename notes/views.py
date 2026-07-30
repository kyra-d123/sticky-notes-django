"""Provide CRUD views for the Sticky Notes application."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display all notes on the application home page."""
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    """Display the details of one note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """Create a note from valid submitted form data."""
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            return redirect("notes:note_detail", pk=note.pk)
    else:
        form = NoteForm()

    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "page_title": "Create Note",
        },
    )


def note_update(request, pk):
    """Update an existing note from valid submitted form data."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            updated_note = form.save()
            return redirect("notes:note_detail", pk=updated_note.pk)
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "note": note,
            "page_title": "Update Note",
        },
    )


def note_delete(request, pk):
    """Delete a note after receiving confirmation from the user."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note},
    )