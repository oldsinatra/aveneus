from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('/about',views.AboutView, name="about"),
    path('all',views.allproperties, name="allproperties"),

    ]
