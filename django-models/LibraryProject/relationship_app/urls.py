from django.urls import path
from . import views

urlpatterns = [
    path("all_books/", views.list_all_books_db, name="all_books"),
    path("class_listbooks/", ListBooksView.as_view(),
         name="all_books_in_library"),
]
