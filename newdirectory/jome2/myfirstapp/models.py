from django.db import models
from django.utils import timezone
# Create your models here.

class studiocoaches(models.Model):
    esm=models.CharField(max_length=20)
    famil=models.CharField(max_length=50)
    tarikhtavalod = models.DateField(default=timezone.now)
    roozayekelas=models.DateField
    saatekelas=models.TimeField
    income_per_hours=models.CharField(max_length=10)



    def __str__(self): 
        return self.famil