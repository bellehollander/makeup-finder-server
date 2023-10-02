from django.db import models



class ProductReview(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)