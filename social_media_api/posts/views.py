from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only the owner to edit or delete."""
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the object's owner
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for handling Post CRUD operations"""
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author to the authenticated user
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for handling Comment CRUD operations"""
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author to the authenticated user
        serializer.save(author=self.request.user)
