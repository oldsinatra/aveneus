from django.shortcuts import render
from rest_framework import generics
from properties.models import Property
from .serializers import PropertySerializer

class PropertyAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

