from rest_framework import serializers
from users.models import EcomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EcomUser
        fields = ['id', 'url', 'email', 'is_staff','first_name', 'is_superuser', 'last_name', 'mobile_no', 'images']


class UserRegisterSerializer(serializers.ModelSerializer):
   
    password2 = serializers.CharField() 

    class Meta:
        model = EcomUser
        fields = ['email','first_name','last_name','mobile_no','images','gender','password','password2']


    def save(self):
        user = EcomUser(email=self.data['email'])

        if self.data['password'] != self.data['password2']:
            raise serializers.ValidationError({'password':'Password must be same'})

        user.set_password(self.data['password'])
        if not self.data['first_name']:
            raise serializers.ValidationError({'first_name':'First name cannot be empty'})
        user.first_name = self.data['first_name']

        if 'last_name' in self.data:
            user.last_name = self.data['last_name']
        if 'mobile_no' in self.data:
            user.mobile_no = self.data['mobile_no']
        if 'images' in self.data:
            user.images = self.data['images']
        if 'gender' in self.data:
            user.gender = self.data['gender']
        user.save()
        return user

