from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return Book.objects.none()

def get_books_in_library(library_name):
    """List all books in a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None