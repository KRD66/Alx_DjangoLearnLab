from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm 

# Create your views here.

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # Redirect to book list after editing
    else:
        form = BookForm(instance=book)

    return render(request, "bookshelf/edit_book.html", {"form": form})