from django.db import models

# Create your models here.


class project(models.Model):
    
    def __str__(self):
        return self.name
    
    reg=models.IntegerField()
    name=models.CharField(max_length=30)
    lat=models.CharField(max_length=40)
    long=models.CharField(max_length=40)
    zoomIn=models.IntegerField(default=12)
    owner=models.CharField(max_length=40)
    careT=models.CharField(max_length=200)
    
class plant(models.Model):
    
    def __str__(self):
        return (str)(self.plantID)

    plantID=models.IntegerField()
    parentProject=models.IntegerField()
    lastChecked=models.CharField(max_length=200)
    typeDetails=models.CharField(max_length=200)
    plantStatus=models.CharField(max_length=30)
    healthDetails=models.CharField(max_length=400)
    lat=models.CharField(max_length=40)
    long=models.CharField(max_length=40)
    
    
    
    