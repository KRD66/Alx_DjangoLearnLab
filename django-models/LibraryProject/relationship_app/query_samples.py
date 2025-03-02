import django
import os

# Set up Django environment if running standalone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return [book.title for book in library.books.all()]

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian.name

# Example usage
if __name__ == "__main__":
    print("Books by George Orwell:", books_by_author("George Orwell"))
    print("Books in City Library:", books_in_library("City Library"))
    print("Librarian of City Library:", librarian_of_library("City Library"))
