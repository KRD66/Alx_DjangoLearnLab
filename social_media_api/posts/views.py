from rest_framework import viewsets, permissions,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model

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

class FeedView(generics.ListAPIView):
    """View to return a feed of posts from followed users"""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return posts from users the authenticated user follows"""
        user = self.request.user
        following_users = user.following.all()  # Get users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
