from django.shortcuts import render
from rest_framework import generics

from records.models import Records
from records.serializers import RecordsSerializer


class DisplayAllRecords(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = RecordsSerializer
    queryset = Records.objects.all()

    def get_queryset(self):
            return Records.objects.all()
