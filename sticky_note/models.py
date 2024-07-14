# sticky_note/models.py
from django.db import models


class StickyNote(models.Model):
    """
    Model representing a sticky note.

    Fields:
    - title: CharField for the note title with a maximum length of 55
    characters.
    - content: TextField for the note content.
    - created_at: DateTimeField sets the current time and date when a note
    is created.

    Relationships:
    - author: ForeignKey representing the author of the created note.

    Methods:
    - No methods have been defined in this model.

    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=55)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Created a ForeignKey for the author's relationship.
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )


class Author(models.Model):
    """
    Model representing the Author of a Sticky Note post.

    Fields:
    - name: CharField for the author's name.

    Methods:
    - No methods are defined in this model.

    :param models.Model: Django's base model class.
    """

    name = models.CharField(max_length=255)
