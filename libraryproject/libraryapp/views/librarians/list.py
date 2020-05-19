import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from libraryapp.models import Librarian
from ..connection import Connection

@login_required
def librarian_list(request):
    all_librarians = Librarian.objects.all()

    template = "librarians/list.html"
    context = {
        'all_librarians': all_librarians
    }

    return render(request, template, context)