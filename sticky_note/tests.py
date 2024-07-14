# sticky_note/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import StickyNote, Author

"""
A testing environment using the imports 'StickyNote' and 'Author' to
setUp test objects. Using the django TestCase to implement testing on
the models and views to check whether their behaviour is as expected.

Testing UseCase:
Models Testing:
- Checking that the note has a title.
- Checking the note has content within it.
Views Testing:
- Test whether note_list returns all created notes as intended.
- Test whether note_detail displays the details of a specific note.
- Test delete_note removes a specific note.
- Test create_note adds a note.
"""


# Create your tests here.
class StickyNoteModelTest(TestCase):
    def setUp(self) -> None:
        # Created an author object.
        author = Author.objects.create(name="Test Author")
        # Created a Note object for testing.
        StickyNote.objects.create(
            title="Test Note", content="This is a test note.", author=author
        )

    def test_note_has_title(self):
        # Test that note object has the expected title.
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        # Test that note object has the expected content.
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class StickyNoteViewTest(TestCase):
    def setUp(self) -> None:
        # Created an author object.
        author = Author.objects.create(name="Test Author")
        # Created a Note object for testing views.
        StickyNote.objects.create(
            title="Test Note", content="This is a test note.", author=author
        )

    def test_note_list_returns_all_notes(self):
        # Tests note_list view returns all notes.
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_displays_specific_note(self):
        # Tests note_detail view displays a specific note.
        note = StickyNote.objects.get(id=1)
        response = self.client.get(reverse("note_detail", args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")

    def test_delete_note_should_remove_item(self):
        # Tests delete_note view removes note.
        notes = StickyNote.objects.all()
        init_length = notes.count()

        note = StickyNote.objects.get(id=1)
        response = self.client.get(reverse("delete_note", args=[note.id]))
        # Final length check
        final_length = StickyNote.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(init_length, final_length)

    def test_create_note_adds_new_note(self):
        # Tests create_note view adds new note.
        initial_note_count = StickyNote.objects.count()
        response = self.client.post(
            reverse("create_note"),
            {
                "title": "New Note",
                "content": "This is a new note.",
            },
        )
        # Updated count check
        updated_note_count = StickyNote.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(initial_note_count, updated_note_count)
