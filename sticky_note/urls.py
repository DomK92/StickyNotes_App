# sticky_note/urls.py
from django.urls import path
from .views import note_list, note_detail, create_note, note_update, delete_note

"""
Contains URL patterns, mapping the URL to the views and how the links
will be displayed and referenced too.
"""
urlpatterns = [
    # URL pattern for displaying a list of all sticky notes
    path("", note_list, name="note_list"),
    # URL pattern for displaying the contents of a specific sticky note
    path("<int:pk>", note_detail, name="note_detail"),
    # URL pattern for creating a new sticky note
    path("new/", create_note, name="create_note"),
    # URL pattern for updating an existing sticky note
    path("<int:pk>/edit", note_update, name="note_update"),
    # URL pattern for deleting a sticky note
    path("<int:pk>/delete/", delete_note, name="delete_note"),
]
