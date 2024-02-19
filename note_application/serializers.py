# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note, Share

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title', 'content']

class NoteUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=False)
    content = serializers.CharField(max_length=1000, required=False)