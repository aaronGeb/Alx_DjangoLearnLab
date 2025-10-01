from django.shortcuts import render,redirect
from django.contrib.auth import login, 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.form import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.

# Register View
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
# logout_view(request):

def logout_view(request):
    logout(request)
    return redirect("login")
# Profile View
@login_required
def profile_view(request):
    return render(request, "profile.html", {"user": request.user})