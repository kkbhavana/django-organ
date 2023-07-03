from django.db import models


# Create your models here.

class Doner(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)
    organ = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    status = models.BooleanField()


    def __str__(self):
        return self.name