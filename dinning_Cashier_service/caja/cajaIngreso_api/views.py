from django.shortcuts import render
from rest_framework import serializers, viewsets
from cajaingreso.models import Caja


class CajaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caja
        fields = '__all__'


class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
