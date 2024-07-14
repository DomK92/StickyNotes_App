# sticky_note/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm


# Create your views here.
def note_list(request):
    """
    View to display a list of existing sticky notes.

    Args:
        request: HTTP request object.
    Returns:
        Returns a rendered template for a list of notes.
    """
    # Created variable takes in the sticky note model which will
    # retrieve all instances of the object.
    notes = StickyNote.objects.all

    # Created a context dictionary which provides data.
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }
    return render(request, "notes/index.html", context)


def note_detail(request, pk):
    """
    View to display details of a specific sticky note.

    Args:
        request: HTTP request object.
        pk: Primary key of the note.

    Returns:
        Returns a rendered template of details for a specific
        sticky note.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def create_note(request):
    """
    View to create a new sticky note.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template of creating a new sticky note.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.Author = request.user
            note.save()
            return redirect("note_list")
    else:
        form = StickyNoteForm()
    return render(request, "notes/stickynote_form.html", {"form": form})


def note_update(request, pk):
    """
    View to update an existing sticky note.

    Args:
        request: HTTP request object.
        pk: Primary key of the note to be updated.

    Returns:
        Rendered template for updating a specific sticky note.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect("note_list")
    else:
        form = StickyNoteForm(instance=note)
    return render(request, "notes/stickynote_form.html", {"form": form})


def delete_note(request, pk):
    """
    View to delete an existing sticky note.

    Args:
        request: HTTP request object.
        pk: Primary key of note to be deleted.

    Returns:
        Redirect to note list after deletion.
    """
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect("note_list")
