from rest_framework import serializers
from products.models import Product, Categories
from users.serializers import UserSerializer
from rest_framework.fields import CurrentUserDefault


class ProductsSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserDefault())
    modified_by = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['id','created_on', 'modified_on', 'created_by', 'modified_by', 'name',
                     'description', 'price','image', 'is_live','category','is_featured']


class CategoriesSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserDefault())
    modified_by = serializers.HiddenField(default=CurrentUserDefault())
    
    class Meta:
        model = Categories
        fields = ['id','created_on', 'modified_on', 'created_by', 'modified_by', 'name',
                     'description', 'image', 'is_live']


class ProductsCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','description', 'price','image',]


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=CurrentUserDefault())
    product = ProductsCartSerializer(read_only=True, many=True)

    class Meta:
        model = Categories
        fields = ['id','modified_on', 'created_by','product']