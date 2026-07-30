"""Test models, forms, URLs, and CRUD views for the notes app."""

from django.test import TestCase
from django.urls import resolve, reverse

from .forms import NoteForm
from .models import Note
from .views import (
    note_create,
    note_delete,
    note_detail,
    note_list,
    note_update,
)


class NoteModelTests(TestCase):
    """Test the behaviour of the Note model."""

    def setUp(self):
        """Create a note used by the model tests."""
        self.note = Note.objects.create(
            title="Model test note",
            content="This note is used to test the Note model.",
        )

    def test_note_is_created(self):
        """Confirm that a note is saved in the test database."""
        self.assertEqual(Note.objects.count(), 1)

    def test_note_fields_are_stored(self):
        """Confirm that the title and content are stored correctly."""
        self.assertEqual(self.note.title, "Model test note")
        self.assertEqual(
            self.note.content,
            "This note is used to test the Note model.",
        )

    def test_note_string_representation(self):
        """Confirm that the note string representation is its title."""
        self.assertEqual(str(self.note), "Model test note")


class NoteFormTests(TestCase):
    """Test validation performed by the NoteForm."""

    def test_form_accepts_valid_data(self):
        """Confirm that a title and content produce a valid form."""
        form = NoteForm(
            data={
                "title": "Valid note",
                "content": "Valid note content.",
            }
        )

        self.assertTrue(form.is_valid())

    def test_form_rejects_missing_title(self):
        """Confirm that the title field is required."""
        form = NoteForm(
            data={
                "title": "",
                "content": "The title has been omitted.",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_form_rejects_missing_content(self):
        """Confirm that the content field is required."""
        form = NoteForm(
            data={
                "title": "Missing content",
                "content": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)


class NoteURLTests(TestCase):
    """Test that note URLs resolve to the correct view functions."""

    def test_note_list_url_resolves(self):
        """Confirm that the home URL resolves to note_list."""
        resolved_view = resolve(reverse("notes:note_list"))
        self.assertEqual(resolved_view.func, note_list)

    def test_note_create_url_resolves(self):
        """Confirm that the create URL resolves to note_create."""
        resolved_view = resolve(reverse("notes:note_create"))
        self.assertEqual(resolved_view.func, note_create)

    def test_note_detail_url_resolves(self):
        """Confirm that the detail URL resolves to note_detail."""
        resolved_view = resolve(
            reverse("notes:note_detail", kwargs={"pk": 1})
        )
        self.assertEqual(resolved_view.func, note_detail)

    def test_note_update_url_resolves(self):
        """Confirm that the update URL resolves to note_update."""
        resolved_view = resolve(
            reverse("notes:note_update", kwargs={"pk": 1})
        )
        self.assertEqual(resolved_view.func, note_update)

    def test_note_delete_url_resolves(self):
        """Confirm that the delete URL resolves to note_delete."""
        resolved_view = resolve(
            reverse("notes:note_delete", kwargs={"pk": 1})
        )
        self.assertEqual(resolved_view.func, note_delete)


class NoteViewTests(TestCase):
    """Test the CRUD views provided by the notes application."""

    def setUp(self):
        """Create a note used by the view tests."""
        self.note = Note.objects.create(
            title="Original title",
            content="Original content.",
        )

    def test_note_list_view(self):
        """Confirm that the list view displays stored notes."""
        response = self.client.get(reverse("notes:note_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")
        self.assertContains(response, "Original title")

    def test_note_detail_view(self):
        """Confirm that the detail view displays the selected note."""
        response = self.client.get(
            reverse("notes:note_detail", kwargs={"pk": self.note.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_detail.html")
        self.assertContains(response, "Original title")
        self.assertContains(response, "Original content.")

    def test_note_create_view_get_request(self):
        """Confirm that a GET request displays the note form."""
        response = self.client.get(reverse("notes:note_create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        self.assertIsInstance(response.context["form"], NoteForm)

    def test_note_create_view_post_request(self):
        """Confirm that valid POST data creates a new note."""
        response = self.client.post(
            reverse("notes:note_create"),
            {
                "title": "Created title",
                "content": "Created content.",
            },
        )

        created_note = Note.objects.get(title="Created title")

        self.assertRedirects(
            response,
            reverse(
                "notes:note_detail",
                kwargs={"pk": created_note.pk},
            ),
        )
        self.assertEqual(Note.objects.count(), 2)

    def test_note_update_view_get_request(self):
        """Confirm that the update page displays the existing note."""
        response = self.client.get(
            reverse("notes:note_update", kwargs={"pk": self.note.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_form.html")
        self.assertContains(response, "Original title")

    def test_note_update_view_post_request(self):
        """Confirm that valid POST data updates an existing note."""
        response = self.client.post(
            reverse("notes:note_update", kwargs={"pk": self.note.pk}),
            {
                "title": "Updated title",
                "content": "Updated content.",
            },
        )

        self.note.refresh_from_db()

        self.assertEqual(self.note.title, "Updated title")
        self.assertEqual(self.note.content, "Updated content.")
        self.assertRedirects(
            response,
            reverse(
                "notes:note_detail",
                kwargs={"pk": self.note.pk},
            ),
        )

    def test_note_delete_view_get_request(self):
        """Confirm that the delete page asks for confirmation."""
        response = self.client.get(
            reverse("notes:note_delete", kwargs={"pk": self.note.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "notes/note_confirm_delete.html",
        )

    def test_note_delete_view_post_request(self):
        """Confirm that a POST request deletes the selected note."""
        response = self.client.post(
            reverse("notes:note_delete", kwargs={"pk": self.note.pk})
        )

        self.assertEqual(Note.objects.count(), 0)
        self.assertRedirects(response, reverse("notes:note_list"))

    def test_missing_note_returns_404(self):
        """Confirm that requesting a nonexistent note returns 404."""
        response = self.client.get(
            reverse("notes:note_detail", kwargs={"pk": 9999})
        )

        self.assertEqual(response.status_code, 404)