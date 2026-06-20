from django.db import models

class Service(models.Model):
    ser_title=models.CharField(max_length=100)
    ser_data=models.TextField()

class About(models.Model):
    ab_title=models.CharField(max_length=100)
    ab_data=models.TextField()
# Create your models here.
