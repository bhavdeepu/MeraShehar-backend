from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet, CategoriesViewSet, CartViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'cart', CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
]