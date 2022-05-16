from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.TextField(max_length=255)
    year = models.IntegerField(default=25)
    selling_price = models.IntegerField(default=0)
    km_driven = models.IntegerField(default=0)
    transmission = models.TextField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=True)  # many to one

    def __str__(self):
        return self.name
