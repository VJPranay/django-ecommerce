from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

