from django.db import models

class Tips(models.Model):
    makeup_skill = models.ForeignKey('MakeupSkill', on_delete=models.CASCADE)
    image = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    