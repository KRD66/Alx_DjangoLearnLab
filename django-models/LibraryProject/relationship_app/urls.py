from django.contrib import admin
from relationship_app import views

# relationship_app/urls.py
from django.urls import path
from relationship_app.views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
    path('register/',views.register_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]