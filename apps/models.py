import imp
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)
    phone = models.CharField(max_length=200)



