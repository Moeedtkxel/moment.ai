from django.db import models


# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=255);

    def __str__(self):
        return str(self.name)
