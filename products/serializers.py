from rest_framework import serializers
from products.models import Product, Categories


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['created_on', 'modified_on', 'created_by', 'modified_by', 'name', 'description', 'price','image']


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['created_on', 'modified_on', 'created_by', 'modified_by', 'name', 'description', 'image']