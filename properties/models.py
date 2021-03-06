from django.db import models
from django.utils.safestring import mark_safe

# # Create your models here.

class Landlord(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Tenant(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=250)
    picture = models.ImageField(null=True, blank=True,upload_to='images/')
    type = models.CharField(max_length=250)
    # landlord = models.CharField(max_length=100)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True, null=True)
    area = models.CharField(max_length=13,default = 1)
    bedrooms = models.CharField(max_length=13,default = 1)
    total_units = models.CharField(max_length=13)
    occupied_units = models.CharField(max_length=13)
    unoccupied_units = models.CharField(max_length=13)

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Property'
        verbose_name_plural = 'Properties' 

    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.title

   
class PropertyTenant(models.Model):
    name = models.CharField(max_length=250)
    property =  models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    landlord =  models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True)
    tenant =  models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True, null=True)
    period  = models.CharField(max_length=250, blank=True, null=True)
    price  = models.CharField(max_length=250, blank=True, null=True)
    amountDue  = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class Agency(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(null=True, blank=True,upload_to='images/')
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)

    class Meta:
        ordering = ["-name"]
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def picture_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.picture.url))
    picture_tag.short_description = 'Picture'

    def __str__(self):
        return self.name

     
 