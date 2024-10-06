from django.db import models
from master.models import Master
from module.models import Module
from sub_module.models import Sub_Module
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, default=None, blank=True)
    product_quantity = models.IntegerField()
    # created_by = models.CharField(max_length=200, default=None, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    product_allocation = models.CharField(max_length=200, default=None, blank=True)
    product_description = models.TextField(default=None, blank=True)
    qr_code_image = models.ImageField(upload_to='qr_codes/',default=None, blank=True, null=True)
    

    class Meta:
        db_table = 'product'  # Custom table name