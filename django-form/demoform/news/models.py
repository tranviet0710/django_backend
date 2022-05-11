import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering='time_create',
        description='Published recently?',
    )
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(1) <= self.time_create <= timezone.now()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500, blank=False, null=False)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
