from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save # Produces a signal if there is any database action.

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    full_name = models.CharField(max_length = 40)
    phone_no = models.CharField(max_length = 10)
    address = models.CharField(max_length = 60)

    def __str__(self):
        return self.user.username

