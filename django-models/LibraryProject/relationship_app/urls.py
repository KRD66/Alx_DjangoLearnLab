# relationship_app/urls.py
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),  # URL for user registration
    path('login/', views.user_login, name='login'),      # URL for user login
    path('logout/', views.user_logout, name='logout'),   # URL for user logout
]