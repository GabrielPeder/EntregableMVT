from django.db import models

class Members(models.Model):
    familiarType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    isEmployed = models.BooleanField()