from django.conf.urls import url, include
from rest_framework import routers

from .views import RegistroViewSet

router = routers.DefaultRouter()
router.register(r'registros', RegistroViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
