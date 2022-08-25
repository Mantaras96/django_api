from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    foundation = models.PositiveIntegerField()

class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)

class Languages(models.Model):
    code = models.CharField(max_length=5)

class Person(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.CharField(max_length=10)
   eye_color = models.CharField(max_length=10)
   language = models.ForeignKey(Languages, on_delete=models.DO_NOTHING)
   species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)


