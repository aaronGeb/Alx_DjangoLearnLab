from bookshelf.models import Book

# Create a book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=1949
)