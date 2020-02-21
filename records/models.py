from django.db import models


class Records(models.Model):
    cam = models.ForeignKey('camera.Camera', null=False, related_name='cameras2', on_delete=models.CASCADE,  default=1)
    driver = models.ForeignKey('driver.Driver', null=False, related_name='drivers2', on_delete=models.CASCADE,  default=1)
    frame_name = models.CharField(max_length=255,null=False)
    timestamp = models.DateTimeField(null=False, )
    pose_yaw = models.FloatField( null=False)
    pose_pitch = models.FloatField(null=False)
    pose_roll = models.FloatField(null=False)
    face_status = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.frame_name)

    def timeago(self):
        from django.utils.timesince import timesince
        return timesince(self.timestamp)
