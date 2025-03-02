# relationship_app/views.py
from django.shortcuts import render
from .models import Book

from django.views.generic import DetailView
from .models import Library
from django.http import HttpResponse

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
    # relationship_app/views.py


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    response_text = "Books Available:\n\n"
    
    for book in books:
        response_text += f"- {book.title} by {book.author.name}\n"
    
    return HttpResponse(response_text, content_type="text/plain")