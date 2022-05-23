from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Property)
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(PropertyTenant)
admin.site.register(Agency)