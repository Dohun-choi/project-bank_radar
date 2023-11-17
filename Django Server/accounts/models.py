from django.contrib.auth.models import AbstractUser
from recommend.models import UserProfile

# Create your models here.
class User(AbstractUser):
    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the instance is being created for the first time
        super().save(*args, **kwargs)  # Save the User instance

        if created:
            UserProfile.objects.create(user=self, nickname=f'unknown{self.id}')