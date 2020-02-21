from rest_framework import serializers

from minuterecords.models import MinuteRecords


class MinuteRecordsSerializer(serializers.ModelSerializer):
    timeago = serializers.DateTimeField(read_only=True)
    vehicle_name = serializers.CharField(source='driver.vehicle.name')

    class Meta:
        model = MinuteRecords
        fields = ('vehicle_name', 'face_status', 'timeago',)
        read_only_fields = ('timeago',)


class DriverDataSerializer(serializers.ModelSerializer):
    timeago = serializers.DateTimeField(read_only=True)
    saferate = serializers.FloatField(read_only=True)
    inactive = serializers.FloatField(read_only=True)
    driver_name = serializers.CharField(source="driver.name", read_only=True)

    class Meta:
        model = MinuteRecords
        fields = ('driver_name', 'saferate', 'inactive', 'timeago',)
        read_only_fields = ('timeago',)


class RecentIncidentSerializer(serializers.ModelSerializer):
    camera_name = serializers.CharField(source="cam.name", read_only=True)
    driver_name = serializers.CharField(source="driver.name", read_only=True)
    timeago = serializers.DateTimeField(read_only=True)

    class Meta:
        model = MinuteRecords
        fields = ('camera_name', 'driver_name', 'face_status', 'timeago', 'timestamp')
