from django.db import models


class MakeupPreferences(models.Model):
    label = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
