from datetime import date

from django.db import models
from django.conf import settings


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, unique=True)
    birth = models.DateTimeField(null=True, blank=True)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    assets = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) 

    age = models.IntegerField(null=True, blank=True)
    age_group = models.IntegerField(null=True, blank=True)
    monthly_income_group = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    assets_group = models.IntegerField(null=True, blank=True)
    
    def save_group_values(self):
        if self.birth:
            today = date.today()
            self.age = today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))
        
        if self.birth:
            self.age_group = (self.age // 10)
        else:
            self.age_group = None
        
        if self.monthly_income:
            self.monthly_income_group = (self.monthly_income // 500000)
        else:
            self.monthly_income_group = None
        
        if self.assets:
            if self.assets < 100_000_000:
                self.assets_group = (self.assets // 10_000_000)
            elif self.assets <= 1_000_000_000:
                self.assets_group = (self.assets // 50_000_000) * 10
            else:
                self.assets_group = 201
        else:
            self.assets_group = None

    def save(self, *args, **kwargs):
        self.save_group_values()
        super().save(*args, **kwargs)


class Travel(models.Model):
    country = models.TextField(unique=True)
    when = models.TextField()
    cost = models.IntegerField()