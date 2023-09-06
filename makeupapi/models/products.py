from django.db import models


class Product(models.Model):
    makeup_preferences = models.ForeignKey('MakeupPreferences', on_delete=models.CASCADE)
    image = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
