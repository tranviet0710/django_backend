# Create your models here.
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title