from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from dajngo.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages


from django.contrib.auth.decorators import user_passes_test, permission_required


# Create your views here.
def list_books(request):
    """function-based view to list all books in the database"""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    """Class-based view to list all books in the specified library"""

    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.objects.all()
        return context


class LoginView(View):
    template_name = "relationship_app/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        # Handle login logic here
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, self.template_name, {"form": form})


class RegisterView(View):
    template_name = "relationship_app/register.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the error below.")
            return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("login")


# --- Role check functions ---
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Views with access control ---
@user_passes_test(is_admin, login_url="login")
def admin_dashboard(request):
    return render(request, "relationship_app/admin_view.html", {"user": request.user})


@user_passes_test(is_librarian, login_url="login")
def librarian_dashboard(request):
    return render(
        request, "relationship_app/librarian_view.html", {"user": request.user}
    )


@user_passes_test(is_member, login_url="login")
def member_dashboard(request):
    return render(request, "relationship_app/member_view.html", {"user": request.user})


# Views to Enforce Permissions
@permission_required("relationship_app.can_add_book")
def can_add_book_view(request):
    return render(request, "relationship_app/can_add_book.html")


@permission_required("relationship_app.can_change_book")
def can_change_book_view(request):
    return render(request, "relationship_app/can_change_book.html")


@permission_required("relationship_app.can_delete_book")
def can_delete_book_view(request):
    return render(request, "relationship_app/can_delete_book.html")
