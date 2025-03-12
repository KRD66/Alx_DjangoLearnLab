from .models import Book
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import viewsets
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly
from  rest_framework.generics import generics

class BookList (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Restrict modification to owners