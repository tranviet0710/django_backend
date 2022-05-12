# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class User(AbstractUser):
    gender = ((0, "Nữ"), (1, "Nam"), (2, "Không xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=gender, default=0)
    address = models.CharField(default='', max_length=255)
