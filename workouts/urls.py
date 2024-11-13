# workouts/urls.py
from django.urls import path
from .views import WorkoutListCreateView
from .views import WeeklyWorkoutsView

urlpatterns = [
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/weekly/', WeeklyWorkoutsView.as_view(), name='weekly-workouts'),
]
