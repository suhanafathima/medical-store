from django.db import models

class Product(models.Model):
    medicine_name = models.CharField(max_length=500)
    quantity_in_stock = models.DecimalField(max_digits=10, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)