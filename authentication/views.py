from django.shortcuts import render

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer, TokenObtainPairSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
