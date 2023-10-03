from django.db import models
from unicodedata import name

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=50)
    cusine=models.CharField(max_length=60)
    price=models.IntegerField()
    