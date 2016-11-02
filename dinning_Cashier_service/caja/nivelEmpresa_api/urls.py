from django.conf.urls import url, include
from rest_framework import routers

from .views import SucursalViewSet

router = routers.DefaultRouter()
router.register(r'sucursal', SucursalViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
