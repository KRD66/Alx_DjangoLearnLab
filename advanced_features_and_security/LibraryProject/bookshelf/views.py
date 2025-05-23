from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm 
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import ExampleForm

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

@csrf_exempt
def api_view(request):
    if request.method == "POST":
        return JsonResponse({"message": "Success"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})