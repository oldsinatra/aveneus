from django.shortcuts import render
# from rest_framework import generics, permissions
from rest_framework import viewsets,permissions
from .models import *
from .serializers import LandlordSerializer, PropertySerializer, PropertyTenantSerializer, TenantSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class LandlordViewSet(viewsets.ModelViewSet):
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class TenantViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class PropertyTenantViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = PropertyTenant.objects.all()
    serializer_class = PropertyTenantSerializer





