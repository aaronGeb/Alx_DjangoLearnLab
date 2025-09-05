from django.urls import path
from . import views
from .views import ListBooksView,list_all_books_db
urlpatterns = [
    path("all_books/", list_all_books_db, name="all_books"),
    path("class_listbooks/", ListBooksView.as_view(),
         name="all_books_in_library"),
]
