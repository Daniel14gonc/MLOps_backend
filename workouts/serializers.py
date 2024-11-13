# workouts/serializers.py
from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'distance', 'time', 'heartrate', 'calories', 'date']
        read_only_fields = ['user']
