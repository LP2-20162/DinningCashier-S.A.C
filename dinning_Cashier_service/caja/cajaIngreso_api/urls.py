from django.conf.urls import url, include
from rest_framework import routers

from .views import CajaViewSet

router = routers.DefaultRouter()
router.register(r'cajas', CajaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
