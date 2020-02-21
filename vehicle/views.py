from django.shortcuts import render
from rest_framework import generics

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer


class DisplayAllVehicles(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def get_queryset(self):
        return Vehicle.objects.all()

