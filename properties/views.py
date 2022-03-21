from django.shortcuts import render
from django.views.generic import ListView
from .models import Property
# Create your views here.

class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'