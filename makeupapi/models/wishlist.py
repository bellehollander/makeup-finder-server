from django.db import models

class Wishlist(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)