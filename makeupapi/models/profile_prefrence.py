from django.db import models

class ProfilePreference(models.Model):
    Profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    MakeupPreferences = models.ForeignKey("MakeupPreferences", on_delete=models.CASCADE)
    


