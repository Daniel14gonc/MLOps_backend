# workouts/views.py
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer
from datetime import timedelta
from django.utils import timezone

class WorkoutListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WeeklyWorkoutsView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener la fecha de hace 7 días
        last_week = timezone.now().date() - timedelta(days=7)
        
        # Filtrar workouts por fecha (últimos 7 días)
        workouts = Workout.objects.filter(date__gte=last_week)

        data = []
        for workout in workouts:
            data.append({
                'id': workout.id,
                'distance': workout.distance,
                'heartrate': workout.heartrate,
                'date': workout.date,
                'user_id': workout.user.id,
                'age': workout.user.age,
                'weight': workout.user.weight,
                'gender': workout.user.gender,
            })

        return Response(data, status=status.HTTP_200_OK)