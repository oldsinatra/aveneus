from django.shortcuts import render
# from django.views.generic import ListView
from .models import Property
# Create your views here.

# class PropertyListView(ListView):
#     model = Property
#     template_name = 'property_list.html'

def home(request):

    properties = Property.objects.all()

    context ={
        'propertyz':properties
              }
    return render(request,'index.html',context)



def allproperties(request):
    properties = Property.objects.all()

    context = {
        'allpropertyz' : properties
        }
    return render(request,'property-grid.html',context)    