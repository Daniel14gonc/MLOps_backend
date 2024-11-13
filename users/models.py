from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import time

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    effort_score = models.FloatField(default=0)
    marathon_time = models.TimeField(default=time(0, 0), null=True, blank=True)