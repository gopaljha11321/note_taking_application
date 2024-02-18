from  django.http import HttpResponse as hr;
from django.shortcuts import render;
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer,NoteSerializer
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import authentication
from .models import Note,Share
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User


def index(request):
    return hr("Note Taking Application")

@api_view(['POST'])
@permission_classes([AllowAny])  
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
@permission_classes([AllowAny])  
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
            serializer.save(owner=request.user) 
            return Response({'message': 'Note created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_note(request, id):
    noteMapping = Share.objects.filter(user_id=request.user, note_id=id).first()
    note={}
    if noteMapping :
        note = Note.objects.filter(id=id).first()
    else: 
        note = get_object_or_404(Note, id=id, owner=request.user)
    serializer = NoteSerializer(note)
    
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def share_note(request):
    note_id = request.data.get('note_id')
    users = request.data.get('users')
    notes = Note.objects.filter(owner=request.user, id=note_id)
    users_exist = User.objects.filter(username__in=users).count() == len(users)
    if users_exist and notes:
        shares = []
        for username in users:
            user = User.objects.filter(username=username).first()
    
            if user is None:
                return Response({'message': f'User {username} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
            share = Share(note_id=note_id, user_id=user)
            shares.append(share)
        Share.objects.bulk_create(shares)
        return Response({'message': 'Share created successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)