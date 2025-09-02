#!/usr/bin/env python3
"""
    Module that defines a class called QuerySamples
"""
from relationship_app.models  import Author, Book, Library, Librarian

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
def librarians_in_libraries():
    """
        Function to get all librarians and their associated libraries
    """
    librarians = Librarian.objects.select_related('library').all()
    librarian_info = {}
    for librarian in librarians:
        librarian_info[librarian.name] = librarian.library.name
    return librarian_info

