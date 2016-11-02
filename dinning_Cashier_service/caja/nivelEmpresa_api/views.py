from rest_framework import serializers, viewsets
from nivelEmpresa.models import Sucursal
#from rest_framework import permissions


class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = '__all__'
        #fields = ('url', 'username', 'email', 'is_staff')


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    #permission_classes = [permissions.IsAuthenticated]
