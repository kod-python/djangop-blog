from django.db import models

# Create your models here.


class Features(models.Model):
    
    name  = models.CharField(max_length=50)
 
    age = models.IntegerField()
    
 
    desc = models.CharField(max_length = 200)
