from bookshelf.models import Book

book = Book.objects.get(id=1)
print(book)
print(book.title, book.author, book.published_date)
