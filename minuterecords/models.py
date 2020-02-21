from django.db import models

# Create your models here.
from django.db.models import Q


class MinuteRecords(models.Model):
    cam = models.ForeignKey('camera.Camera', null=False, related_name='cameras', on_delete=models.CASCADE, default=1)
    driver = models.ForeignKey('driver.Driver', null=False, related_name='drivers', on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(null=False)
    face_status = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.face_status)

    def timeago(self):
        from django.utils.timesince import timesince
        return timesince(self.timestamp)

    def saferate(self):
        result = MinuteRecords.objects.filter(face_status='Active', driver=self.driver).count()
        if result != 0:
            total = MinuteRecords.objects.filter(driver=self.driver).count()
            result = (result / total) * 100
            return result

    def inactive(self):
        result = MinuteRecords.objects.filter(~Q(face_status='Active'), driver=self.driver).count()
        return result
