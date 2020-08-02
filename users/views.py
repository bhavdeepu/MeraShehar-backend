from django.shortcuts import render
from users.models import EcomUser
from rest_framework import serializers, viewsets
from users.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = EcomUser.objects.all()
    serializer_class = UserSerializer