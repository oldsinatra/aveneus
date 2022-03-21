from rest_framework import serializers
from properties.models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('title', 'type', 'landlord', 'total_units','occupied_units','unoccupied_units')