# workouts/models.py
from django.conf import settings
from django.db import models

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    distance = models.FloatField()  # en kilómetros
    time = models.DurationField()   # en formato HH:MM:SS
    heartrate = models.IntegerField()  # promedio en bpm
    calories = models.FloatField(null=True, blank=True)  # opcional
    date = models.DateField()  # Fecha del workout

    def __str__(self):
        return f"Workout on {self.date} by {self.user.username}"