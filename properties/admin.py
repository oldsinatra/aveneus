from django.contrib import admin
from .models import *


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title','picture_tag','landlord', 'tenant','area']

class AgencyAdmin(admin.ModelAdmin):
    list_display = ['name','picture_tag','email', 'phone','address']

# Register your models here.
admin.site.register(Property,PropertyAdmin)
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(PropertyTenant)
admin.site.register(Agency,AgencyAdmin)