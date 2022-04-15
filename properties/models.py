from django.db import models

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
    type = models.CharField(max_length=250)
    # landlord = models.CharField(max_length=100)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True, null=True)
    total_units = models.CharField(max_length=13)
    occupied_units = models.CharField(max_length=13)
    unoccupied_units = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-title"]
        verbose_name = 'Property'
        verbose_name_plural = 'Properties' 

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
