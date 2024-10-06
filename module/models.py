from django.db import models
from master.models import Master


# Create your models here.
class Module(models.Model):
    """Model representing a topic."""

    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    warehouse_id = models.IntegerField(primary_key=True)
    warehouse_name = models.CharField(max_length=100)
    associated_plant = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.TextField()
    state = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    storage_capacity = models.IntegerField()
    temperature_control = models.CharField(max_length=100,choices=CHOICES)
    hazardous_material = models.CharField(max_length=100,choices=CHOICES)
    # securityfeatures = models.TextField()
    securityfeatures = models.CharField(max_length=100)
    

    class Meta:
        db_table = 'module'  # Custom table name
