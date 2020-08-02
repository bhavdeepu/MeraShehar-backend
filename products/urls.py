from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoriesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]