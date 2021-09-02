from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    uid = serializers.CharField(max_length=255)
    balance = serializers.CharField(max_length=255)
    hold = serializers.CharField(max_length=255)
    status = serializers.BooleanField()