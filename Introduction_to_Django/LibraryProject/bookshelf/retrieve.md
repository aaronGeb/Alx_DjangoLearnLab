from bookshelf.models import Book

book = Book.objects.all()
print(book)
print(book.title, book.author, book.published_date)
