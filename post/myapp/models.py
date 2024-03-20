from django.db import models

# Create your models here.


class Features(models.Model):
    
    name  = models.CharField(max_length=50)
 
    age = models.IntegerField()
    
 
    desc = models.CharField(max_length = 200)
    
    

class Infos:
    id : int
    
    name : str
    
    age : int
    
    desc : str
    
    wealth : int
    
    bool : True
    
        
