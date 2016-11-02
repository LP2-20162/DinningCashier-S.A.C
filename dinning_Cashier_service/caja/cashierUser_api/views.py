from rest_framework import serializers, viewsets
from cashierUser.models import UsuarioCajero
#from rest_framework import permissions


class UsuarioCajeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioCajero
        fields = '__all__'
        #fields = ('url', 'username', 'email', 'is_staff')


class UsuarioCajeroViewSet(viewsets.ModelViewSet):
    queryset = UsuarioCajero.objects.all()
    serializer_class = UsuarioCajeroSerializer
