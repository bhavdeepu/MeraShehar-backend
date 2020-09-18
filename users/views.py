from django.shortcuts import render
from users.models import EcomUser
from rest_framework import viewsets
from users.serializers import UserSerializer, UserRegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = EcomUser.objects.all()
    # serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )


    def get_permissions(self):
        if self.request.method in ['GET','PATCH','PUT']:
            return [IsAuthenticated(),]
        else:
            return [AllowAny(),]

    def get_serializer_class(self):
        print ("int o get_serializer_class==",self.action)
        if self.action in ['create']:
            return UserRegisterSerializer
        else:
            return UserSerializer

    @action(methods=['get'], detail=False,
            url_path='currentuser', url_name='currentuser')
    def currentuser(self, request):
        # users_data = UserSerializer(request._user,context={'request': request}).data
        users_data = self.get_serializer(request._user,context={'request': request}).data
        return Response(users_data, status=status.HTTP_200_OK)