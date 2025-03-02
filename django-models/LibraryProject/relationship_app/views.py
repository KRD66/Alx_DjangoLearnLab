# relationship_app/views.py
from django.shortcuts import render, redirect
from .models import Book

from django.views.generic import DetailView
from .models import Library
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
    # relationship_app/views.py


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    response_text = "Books Available:\n\n"
    
    for book in books:
        response_text += f"- {book.title} by {book.author.name}\n"
    
    return HttpResponse(response_text, content_type="text/plain")

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to the home page or any other page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout View 
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to the home page or any other page
