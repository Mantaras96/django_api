from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    foundation = models.PositiveIntegerField()


class User(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    foundation = models.PositiveIntegerField()
