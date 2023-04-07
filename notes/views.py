from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .forms import NotesForm
from .models import Notes


class NoteCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'


# def list_view(response):
#     notes = Notes.objects.all()
#     return render(response, 'notes/notes_list.html', {'notes': notes})
