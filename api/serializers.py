from api.models import Landlord, Property, PropertyTenant, Tenant
from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('title', 'type', 'total_units','occupied_units','unoccupied_units')

class LandlordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landlord
        fields = ('name', 'email', 'phone','address')

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('name', 'email', 'phone','address')

class PropertyTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyTenant
        fields = ('name', 'property', 'landlord','tenant','period','price','amountDue')



