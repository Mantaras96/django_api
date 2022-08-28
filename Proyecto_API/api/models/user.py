from django.db import models
from .languages import Languages

class User (models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField();
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    language = models.ForeignKey(Languages, on_delete=models.DO_NOTHING)
    date_birth = models.DateField();
    created_at = models.DateField();