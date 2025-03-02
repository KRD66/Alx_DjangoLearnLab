
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # URL for user login
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for user logout
]