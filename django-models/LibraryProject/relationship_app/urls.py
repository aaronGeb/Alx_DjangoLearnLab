from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView
from .views import LoginView, RegisterView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path("all_books/", list_books, name="all_books"),
    path("class_listbooks/", LibraryDetailView.as_view(), name="all_books_in_library"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path(
        "register/",
        RegisterView.as_view(template_name="relationship_app/register.html"),
        name="register",
    ),
    path("register/", views.register, name="register"),
    path(
        "",
        TemplateView.as_view(template_name="relationship_app/home.html"),
        name="home",
    ),
    path("librarian_dashboard/", views.librarian_dashboard, name="librarian_dashboard"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("member_dashboard/", views.member_dashboard, name="member_dashboard"),
]
