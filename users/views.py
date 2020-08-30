from django.shortcuts import render
from users.models import EcomUser
from rest_framework import serializers, viewsets
from users.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = EcomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


    @action(methods=['get'], detail=False,
            url_path='currentuser', url_name='currentuser')
    def currentuser(self, request):
        # print ("adasd===",self.request._user.id)
        users_data = UserSerializer(request._user,context={'request': request}).data
        return Response(users_data, status=status.HTTP_200_OK)

        # return 