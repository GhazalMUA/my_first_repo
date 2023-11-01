from django.db import models

# Create your models here.

class studiocoaches(models.Model):
    esm=models.CharField(max_length=20)
    famil=models.CharField(max_length=50)
    tarikhtavalod=models.DateField
    roozayekelas=models.DateField
    saatekelas=models.TimeField
    income_per_hour=models.CharField(max_length=10)