from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    landlord = models.CharField(max_length=100)
    total_units = models.CharField(max_length=13)
    occupied_units = models.CharField(max_length=13)
    unoccupied_units = models.CharField(max_length=13)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "temp_user"    