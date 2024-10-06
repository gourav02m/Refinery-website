from django.db import models

# Create your models here.
class Master(models.Model):
    """Model representing a topic."""

    plant_id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    plant_name = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.TextField()
    state = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    capacity = models.IntegerField()
    establishment = models.DateField()
    compliance_certification = models.CharField(max_length=100)
    operating_hours = models.IntegerField()
    

    class Meta:
        db_table = 'master'  # Custom table name

    