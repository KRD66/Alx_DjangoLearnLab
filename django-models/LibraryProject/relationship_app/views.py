from django.shortcuts import render
from .models import Book
from .models import Library

from django.http import HttpResponse


def book_list(request):
    books = Book.objects.all()
    book_list_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_list_text, content_type="text/plain")


from django.views.generic import DetailView
from django.shortcuts import get_object_or_404



class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
