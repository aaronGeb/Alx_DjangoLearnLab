from bookshelf.models import Book

books = Book.objects.all()
print(books)