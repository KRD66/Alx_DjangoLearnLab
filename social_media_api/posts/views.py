from rest_framework import viewsets, permissions,generics,status,permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment , Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType



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

class LikePostView(APIView):
    """View for liking a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """Handles liking a post"""
        
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        
        # Get or create a like object to prevent duplicate likes
        like, created = Like.objects.get_or_create(user=user, post=post)
        
        
        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


        # Create a notification for the post author (if not the same user)
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )

        return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)
    


class UnlikePostView(APIView):
    """View for unliking a post"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """Handles unliking a post"""
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        # Check if the like exists
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Delete the like
        like.delete()

        return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
