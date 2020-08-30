from rest_framework import serializers
from users.models import EcomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EcomUser
        fields = ['id', 'url', 'email', 'is_staff','first_name','is_superuser']