#from django.shortcuts import render

from rest_framework import serializers, viewsets
from caja.models import Registro
#from rest_framework import permissions


class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro
        fields = '__all__'
        #fields = ('url', 'username', 'email', 'is_staff')


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    #permission_classes = [permissions.IsAuthenticated]
