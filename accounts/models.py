from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null = True, blank = True)

    @property
    def user(self):
        return User.objects.get(pk = self.user_id)


