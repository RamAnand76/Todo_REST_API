from django.shortcuts import render
from rest_framework import generics, status
from .models import Todo
from .serializers import TodoSerializer, UserSerializer, TokenSerializer, UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    #permission_classes = [IsAuthenticated]

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        token_serializer = TokenSerializer({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user': user
        })
        return Response(token_serializer.data, status=status.HTTP_200_OK)
    
