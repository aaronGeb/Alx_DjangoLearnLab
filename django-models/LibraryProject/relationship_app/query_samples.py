#!/usr/bin/env python3
"""
    Module that defines a class called QuerySamples
"""
from relationship_app.models import Author, Book, Library, Librarian


def get_books_by_author(author_name):
    """
    Return all books written by a given author.
    """
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def get_books_in_library(library_name):
    """
    Return all books available in a specific library.
    """
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    """
    Return the librarian assigned to a specific library.
    """
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
