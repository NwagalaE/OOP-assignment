from datetime import datetime
from unittest.util import _MAX_LENGTH
from xml.etree.ElementTree import TreeBuilder
from rest_framework import serializers
from rest_framework.response import Response
from .models import Timer
from django.db.models.fields import DurationField

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = [
            'id',
            'title',
            'activity_time',
            'break_time',
            'date',
            'take_note'
        ]

class RegisterTimeSerialer(serializers.ModelSerializer):
    activity_time = serializers.DurationField()
    break_time = serializers.DurationField()
    date = serializers.DateField()
    title = serializers.CharField(max_length=20)
    take_note = serializers.CharField()
    class Meta:
        model = Timer
        fields = ('id','title','activity_time','break_time','take_note','date')
        extra_kwargs = {
            'activity_time':{'required': True},
            'break_time':{'required': True},
            'title': {'required': True}
        }
    def create(self, validated_data):
        timer = Timer.objects.create(
            title = validated_data['title'],
            activity_time = validated_data['activity_time'],
            break_time = validated_data['break_time'],
            take_note = validated_data['take_note'],
            date = validated_data['date']
        )
        timer.save()
        return timer










