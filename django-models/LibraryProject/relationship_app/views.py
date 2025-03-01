from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library


def book_list(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Template to render
    context_object_name = 'library'  # Pass library instance to template