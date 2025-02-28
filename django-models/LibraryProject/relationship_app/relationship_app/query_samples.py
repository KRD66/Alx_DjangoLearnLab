import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2️⃣ List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3️⃣ Retrieve the librarian for a library
def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Sample Data Insertion (Run this once)
def create_sample_data():
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="John Doe", library=library)

if __name__ == "__main__":
    create_sample_data()

    print("Books by J.K. Rowling:", list(get_books_by_author("J.K. Rowling")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_of_library("Central Library"))
