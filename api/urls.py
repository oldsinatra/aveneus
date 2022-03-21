from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('landlords', LandlordViewSet, basename='landlords')
router.register('tenants', TenantViewSet, basename='tenants')
router.register('propertytenants',PropertyTenantViewSet, basename='propertytenants')
router.register('properties', PropertyViewSet, basename='properties')
urlpatterns = router.urls


# urlpatterns = [
#     # path('<int:pk>/', DetailTodo.as_view()),
#     path('', PropertyAPIView.as_view()),
# ]

