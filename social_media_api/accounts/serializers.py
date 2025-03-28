from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()  # Get the custom user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Ensure user creation
        Token.objects.create(user=user)  # Generate auth token for new user
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



class LoginSerializer(serializers.Serializer):
    """Serializer for user login and authentication"""
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        
        token, _ = Token.objects.get_or_create(user=user)  # Ensure token is created
        return {'user': user, 'token': token.key}
