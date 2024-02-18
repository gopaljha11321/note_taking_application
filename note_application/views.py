from  django.http import HttpResponse as hr;
from django.shortcuts import render;
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer,NoteSerializer
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import authentication
from .models import Note
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes


def index(request):
    return hr("Note Taking Application")

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated access
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response({'error': 'Username or email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow unauthenticated access
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            print(user,'user')
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_note(request):
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Associate the note with the authenticated user
            return Response({'message': 'Note created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_note(request, id):
    # Retrieve the note by ID, ensuring that it belongs to the authenticated user
    print(id)
    note = get_object_or_404(Note, id=id, owner=request.user)
    
    # Serialize the note data
    serializer = NoteSerializer(note)
    
    # Return the serialized note data
    return Response(serializer.data)