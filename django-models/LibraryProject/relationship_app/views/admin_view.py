from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


@user_passes_test(is_admin, login_url="login")
def admin_dashboard(request):
    return render(request, "admin_dashboard.html", {"user": request.user})
