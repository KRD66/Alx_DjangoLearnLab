
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books , register 
from .views import  LibraryDetailView , admin_view, librarian_view, member_view

urlpatterns = [
    # Authentication URLs
    
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for user logout
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]