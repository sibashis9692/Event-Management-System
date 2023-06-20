from django.db import models

# Create your models here.
class sibashisevents(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(null=True, max_length=50)
    tittle=models.CharField(null=True, max_length=50)
    description=models.CharField(null=True, max_length=1000)
    date=models.CharField(null=True, max_length=50)
    cost=models.CharField(null=True, max_length=50)
    location=models.CharField(null=True, max_length=50)

class sibashislocation(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(null=True, max_length=100)
    address=models.CharField(null=True, max_length=100)
    manager=models.CharField(null=True, max_length=100)
    email=models.CharField(null=True, max_length=100)

class sibashislogin(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(null=True, max_length=50)
    password=models.CharField(null=True, max_length=50)