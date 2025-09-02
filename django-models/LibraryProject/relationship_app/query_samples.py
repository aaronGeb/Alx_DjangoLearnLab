#!/usr/bin/env python3
"""
    Module that defines a class called QuerySamples
"""
from relationship_app.models import Author, Book, Library, Librarian


def list_all_books_in_library():
    """
    Function that lists all the books in a library
    """
    """
    Function to list all libraries with their books
    """
    libraries = Library.objects.all()
    library_books = {}
    for library in libraries:
        library_books[library.name] = library.books.all()
    return library_books
