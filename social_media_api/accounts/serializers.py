from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

User = get_user_model().objects.create_user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {'password': {'write_only': True}}


def create(self, validated_data):
        # Create the user properly using create_user()
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        
        # Add additional fields if they exist
        if 'bio' in validated_data:
            user.bio = validated_data['bio']
        if 'profile_picture' in validated_data:
            user.profile_picture = validated_data['profile_picture']
        
        user.save()
        Token.objects.create(user=user)  # Create auth token
        return user
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        Token, _ = Token.objects.get_or_create(user=user)  # Ensure token is created
        return data


