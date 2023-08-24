# TODO: опишите сериализаторы
from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name']

    # name = serializers.CharField()
    # latitude = serializers.FloatField()
    # longitude = serializers.FloatField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
    # id = serializers.FloatField()
    # value = serializers.FloatField()
