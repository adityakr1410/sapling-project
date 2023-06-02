from django.db import models

# Create your models here.


class project(models.Model):
    
    def __str__(self):
        return self.name
    
    reg=models.IntegerField()
    name=models.CharField(max_length=30)
    longitude=models.CharField(max_length=40)
    latitude=models.CharField(max_length=40)
    ownerUsername=models.CharField(max_length=40)
    careTakerDetails=models.CharField(max_length=200)
    
class plant(models.Model):
    
    def __str__(self):
        return (str)(self.plantID)

    plantID=models.IntegerField()
    plantStatus=models.CharField(max_length=30)
    lastChecked=models.CharField(max_length=200)
    typeDetails=models.CharField(max_length=200)
    parentProject=models.IntegerField()
    