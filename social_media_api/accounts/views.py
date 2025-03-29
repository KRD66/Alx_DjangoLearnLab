from rest_framework import generics, permissions, status,viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login , get_user_model
from .serializers import UserSerializer, LoginSerializer, CustomUser
from rest_framework.decorators import action


User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username
            })
        return Response(
            {'error': 'Invalid Credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
        
class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for user actions including follow/unfollow"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def follow(self, request, pk=None):
        """Allows a user to follow another user"""
        user_to_follow = self.get_object()
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.follow(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."})

    @action(detail=True, methods=['POST'])
    def unfollow(self, request, pk=None):
        """Allows a user to unfollow another user"""
        user_to_unfollow = self.get_object()
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."})
