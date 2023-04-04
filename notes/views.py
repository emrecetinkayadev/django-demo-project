from django.shortcuts import render

from .models import Notes


def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return render(request, 'notes/notes_404.html', {})
    return render(request, 'notes/notes_detail.html', {'note': note})
