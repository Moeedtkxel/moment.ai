from django.shortcuts import render
from rest_framework import generics

from camera.models import Camera
from camera.serializers import CameraSerializer


class DisplayAllCameras(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CameraSerializer
    queryset = Camera.objects.all()

    def get_queryset(self):
            return Camera.objects.all()
