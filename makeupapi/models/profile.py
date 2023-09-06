from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    makeup_skill = models.ForeignKey('MakeupSkill', on_delete=models.CASCADE)


    

