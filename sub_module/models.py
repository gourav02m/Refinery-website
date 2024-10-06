from django.db import models
from module.models import Module

# Create your models here.
class Sub_Module(models.Model):
    """Model representing a topic."""

    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    SECTION = [
    	('Cold Storage','Cold Storage'),
    	('Dry Storage','Dry Storage'),

    ]
    ITEMS = [

    	('Petroleum','Petroleum'),
    	('Lubricants','Lubricants'),

    ]

    section_id = models.IntegerField(primary_key=True)
    section_name = models.CharField(max_length=100)
    associated_warehouse = models.CharField(max_length=100)
    section_type= models.CharField(max_length=100,choices=SECTION)
    section_capacity = models.IntegerField()
    temperature_requirement	 = models.IntegerField()
    # hazardous_material = models.CharField(max_length=100,choices=CHOICES)
    stored_item_types = models.CharField(max_length=100,choices=ITEMS)
    access_control = models.CharField(max_length=100,choices=CHOICES)
    special_handling = models.CharField(max_length=100)
    safety_requirements = models.CharField(max_length=100)
    

    class Meta:
        db_table = 'sub_module'  # Custom table name
