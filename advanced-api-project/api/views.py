from django.shortcuts import render
from rest_framework import generics , permissions , filters , serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from datetime import datetime
from django_filters import rest_framework as django_filters
class BookListView(generics.ListAPIView):  # GET all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['author__name']
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter] 
    filterset_fields = ['title', 'author__name', 'publication_year']  # Allow filtering by these fields
    ordering_fields = ['title', 'publication_year']  

class BookCreateView(generics.CreateAPIView):  # POST a new book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        publication_year = serializer.validated_data['publication_year']
        if publication_year > datetime.now().year:
            raise serializers.ValidationError({'publication_year': "publication year can't be in the future."})
        serializer.save()

class BookDetailView(generics.RetrieveAPIView):  # GET a single book by ID
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookUpdateView(generics.UpdateAPIView):  # PUT/PATCH an existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class BookDeleteView(generics.DestroyAPIView):  # DELETE a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    