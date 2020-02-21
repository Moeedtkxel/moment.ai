from rest_framework import serializers
from records.models import Records


class RecordsSerializer(serializers.ModelSerializer):
    timeago = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Records
        fields = '__all__'
        read_only_fields = ('timeago',)
