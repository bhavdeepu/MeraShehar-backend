from products.models import Product, Categories
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.urls import reverse

from products.serializers import ProductsSerializer, CategoriesSerializer
from users.permission import IsSuperUserPermission
from users.serializers import UserSerializer
from users.models import EcomUser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny, )

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny(),]
        else:
            return [IsAuthenticated(), IsSuperUserPermission()]

    def get_queryset(self):
        all_cat = int(self.request.query_params.get("all", 0))
        futr = int(self.request.query_params.get("futr", 0))
        cat_id = self.request.query_params.get("cat")
        key = {}
        if not all_cat:
            key['is_live'] = True 
        if futr:
            key['is_featured'] = True
        if cat_id and cat_id != 'no':
            key['category_id'] = int(cat_id)
        if futr and not(cat_id and cat_id != 'no'):
            key['is_featured'] = True

        queryset = Product.objects.filter(**key).select_related('category','created_by')

        return queryset

    def perform_update(self, serializer):
        instance = self.get_object()
        key = {
            'modified_by_id': self.request.user.id,
            'created_by_id': self.request.user.id,
        }

        if "name" in self.request.data.keys():
            key['name'] = self.request.data['name']
        
        if "description" in self.request.data.keys():
            key['description'] = self.request.data['description']

        if "image" in self.request.data.keys():
            key['image'] = self.request.data['image']

        if "is_live" in self.request.data.keys():
            key['is_live'] = self.request.data['is_live']

        if "is_featured" in self.request.data.keys():
            key['is_featured'] = self.request.data['is_featured']
        obj = serializer.save(**key)
        return obj

    def perform_create(self, serializer):
        
        key = {
            'modified_by': self.request.user,
            'created_by': self.request.user,
            'name': self.request.data['name']
        }

        if "description" in self.request.data.keys():
            key['description'] = self.request.data['description']

        if "image" in self.request.data.keys():
            key['image'] = self.request.data['image']

        serializer.is_valid(raise_exception=True)
        obj = serializer.save(**key)
        return obj

    @action(methods=['patch'], detail=True,
        url_path='change-status', url_name='change-status')
    def change_status(self, request, pk):
        obj = self.get_object()
        obj.is_live = not obj.is_live
        obj.save()
        return Response(ProductsSerializer(obj,context={'request': request}).data, status=status.HTTP_200_OK)

    @action(methods=['patch'], detail=True,
        url_path='change-featured', url_name='change-featured')
    def change_featured(self, request, pk):
        obj = self.get_object()
        obj.is_featured = not obj.is_featured
        obj.save()
        return Response(ProductsSerializer(obj,context={'request': request}).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True,
        url_path='categories-option', url_name='categories-option')
    def categories_option(self, request, pk):
        pro_obj = self.get_object()
        query = Categories.objects.all().values_list('name','id')
        result_final = {'label':pro_obj.category.name,'value':pro_obj.category.id}
        result = []
        for obj in query:
            result.append({'label':obj[0],'value':obj[1]})

        return Response({'option':result,'default':result_final}, status=status.HTTP_200_OK)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny, )

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny(),]
        else:
            return [IsAuthenticated(), IsSuperUserPermission()]

    def get_queryset(self):
        all_cat = int(self.request.query_params.get("all", 0))
        key = {}
        if not all_cat:
            key['is_live'] = True       

        queryset = Categories.objects.filter(**key).select_related('created_by','modified_by')

        return queryset

    def perform_update(self, serializer):

        instance = self.get_object()

        key = {
            'modified_by_id': self.request.user.id,
            'created_by_id': self.request.user.id
        }

        if "name" in self.request.data.keys():
            key['name'] = self.request.data['name']
        
        if "description" in self.request.data.keys():
            key['description'] = self.request.data['description']

        if "image" in self.request.data.keys():
            key['image'] = self.request.data['image']

        if "is_live" in self.request.data.keys():
            key['is_live'] = self.request.data['is_live']

        obj = serializer.save(**key)
        return obj

    def perform_create(self, serializer):
        
        key = {
            'modified_by': self.request.user,
            'created_by': self.request.user,
            'name': self.request.data['name']
        }

        if "description" in self.request.data.keys():
            key['description'] = self.request.data['description']

        if "image" in self.request.data.keys():
            key['image'] = self.request.data['image']

        serializer.is_valid(raise_exception=True)
        obj = serializer.save(**key)
        return obj

    @action(methods=['patch'], detail=True,
        url_path='change-status', url_name='change-status')
    def change_status(self, request, pk):
        obj = self.get_object()
        obj.is_live = not obj.is_live
        obj.save()
        return Response(CategoriesSerializer(obj,context={'request': request}).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False,
        url_path='option', url_name='option')
    def option(self, request):
        query = Categories.objects.all().values_list('name','id')
        result = []
        for obj in query:
            result.append({'label':obj[0],'value':obj[1]})

        return Response(result, status=status.HTTP_200_OK)
