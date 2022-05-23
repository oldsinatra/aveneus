from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

# class PropertyListView(ListView):
#     model = Property
#     template_name = 'property_list.html'
@login_required
def home(request):
    properties = Property.objects.all()
    context ={'propertyz':properties}
    return render(request,'index.html',context)

@login_required
def PropertyGrid(request):
    properties = Property.objects.all()
    '''context ={'propertyz':properties}'''
    return render(request,'property-grid.html',{'propertyz':properties})
   
def RegisterView(request):
    return render(request,'register.html')

def AboutView(request):
    return render(request,'about.html')

@login_required
def AgencyView(request):
    agencies = Agency.objects.all()
    context = {'agencyz':agencies}
    return render(request,'agency-grid.html',context)
