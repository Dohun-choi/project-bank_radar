from datetime import date

from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth = models.DateTimeField()
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    assets = models.DecimalField(max_digits=15, decimal_places=2) 

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age