from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from minuterecords.models import MinuteRecords
from minuterecords.serliazers import MinuteRecordsSerializer, DriverDataSerializer, RecentIncidentSerializer


class DisplayMinuteRecordsById(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = MinuteRecordsSerializer
    queryset = MinuteRecords.objects.all()

    def get_queryset(self):
        driver_id = self.request.query_params.get("driver_id")
        if driver_id:
            return MinuteRecords.objects.filter(driver=driver_id, ).filter(~Q(face_status='Active'))
        else:
            return MinuteRecords.objects.filter(~Q(face_status='Active'))


class DisplayDriverData(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = DriverDataSerializer
    queryset = MinuteRecords.objects.all()

    def get_queryset(self):
        return MinuteRecords.objects.all().distinct('driver__name')


class DisplayRecentIncidents(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RecentIncidentSerializer
    queryset = MinuteRecords.objects.all()

    def get_queryset(self):
        return MinuteRecords.objects.filter(~Q(face_status='Active')).order_by('driver__name', '-timestamp').distinct(
            'driver__name')
