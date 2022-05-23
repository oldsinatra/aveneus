from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name='home'),
    # path('/about',views.AboutView, name="about"),
    path('allprops/',views.PropertyGrid,name = "allproperties"),
    path('register/',views.RegisterView,name="register"),
    path('about/',views.AboutView,name = "about"),
    path('agencies/',views.AgencyView,name="agencies"),
    ]
