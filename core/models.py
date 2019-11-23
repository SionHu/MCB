from django.db import models

# Create your models here.

class mcb(models.Model):
    name = models.CharField(max_length = 70)
    age= models.IntegerField()
