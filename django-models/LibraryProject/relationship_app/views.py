from django.shortcuts import render
from django.http import HttpResponse
from relationship.models import Book
from django.views.generic import ListView, DetailView


# Create your views here.
def list_all_books_db(request):
    """function-based view to list all books in the database"""
    books = Book.objects.all()
    output_lines = []
    for book in books:
        output_lines.append(f"Title: {book.title}, Author: {book.author.name}")
    response_text = "\n".join(output_lines)
    return HttpResponse(response_text, content_type="text/plain")


class ListBooksView(DetailView):
    """Class-based view to list all books in the specified library"""

    model = Library
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.objects.all()
        return context
