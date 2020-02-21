from django.shortcuts import render
from rest_framework import generics

from driver.models import Driver
from driver.serializers import DriverSerializer


class DisplayAllDrivers(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    def get_queryset(self):
            return Driver.objects.all()
