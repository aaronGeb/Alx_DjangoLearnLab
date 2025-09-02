#!/usr/bin/env python3
"""
    Module that defines a class called QuerySamples
"""
from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Function to query books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


def list_libraries_with_books():
    """
    Function to list all libraries with their books
    """
    libraries = Library.objects.all()
    library_books = {}
    for library in libraries:
        library_books[library.name] = library.books.all()
    return library_books


def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Librarian.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Librarian.DoesNotExist:
        print(f"Library {library_name} does not exist")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library {library_name}")
        return None
