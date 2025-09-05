from django.urls import path
from . import views
#from .views import ListBooksView,list_all_books_db
from .views import list_books, LibraryDetailView
urlpatterns = [
    path("all_books/", list_books, name="all_books"),
    path("class_listbooks/", LibraryDetailView.as_view(),
         name="all_books_in_library"),
]


