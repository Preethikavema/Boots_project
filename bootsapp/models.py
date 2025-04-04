from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quality = models.CharField(max_length=100,default='Unknown') 
    quantity = models.IntegerField(default=10)
def __str__(self):
    return self.name

