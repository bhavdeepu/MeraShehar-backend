from django.contrib import admin

from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('', include(router.urls)),
    # path('users/', include('users.urls')),
    path('', include('products.urls')),
    path('api-auth/', include('rest_framework.urls'))
    # path(r'^favicon\.ico$',RedirectView.as_view(url='/media/favicon.ico')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
