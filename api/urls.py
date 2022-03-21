from django.urls import path
from .views import PropertyAPIView

urlpatterns = [path('', PropertyAPIView.as_view()),
]
