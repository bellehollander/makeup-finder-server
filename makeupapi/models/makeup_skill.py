from django.db import models

class MakeupSkill(models.Model):
    label = models.CharField(max_length=50)

   