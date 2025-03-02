
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import book_list, LibraryDetailView

urlpatterns = [
    # Authentication URLs
    
    path('books/', book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for user logout
]