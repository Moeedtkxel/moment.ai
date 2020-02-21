from django.db import models


# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    vehicle = models.ForeignKey('vehicle.Vehicle', null=False, related_name='vehicle2', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
