from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return self.email

        #iufyufyufiyfyuf