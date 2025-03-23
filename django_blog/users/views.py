from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# User Registration View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("profile")  # Redirect to profile page
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")  # Redirect to profile page
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect("login")

# User Profile View (Only for Logged-in Users)
@login_required
def profile(request):
    return render(request, "users/profile.html")
