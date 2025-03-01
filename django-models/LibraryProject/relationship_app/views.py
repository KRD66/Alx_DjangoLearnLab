from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

def book_list(request):
    books = Book.objects.all()
    book_details = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(f"<pre>{book_details}</pre>")  # Displays books as plain text


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  # Ensure you create this template
    context_object_name = "library"