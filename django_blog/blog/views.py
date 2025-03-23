from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Login View (using Django's built-in view)
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

# Logout View (using Django's built-in view)
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

# Profile View
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'registration/profile.html', {'user': request.user})