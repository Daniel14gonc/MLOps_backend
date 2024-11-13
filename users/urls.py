from django.urls import path
from .views import UserCreateView, UserDetailView, BulkUpdateEffortScoreView, BulkUpdateMarathonTimeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('details/', UserDetailView.as_view(), name='user-detail'),
    path('bulk-update-effort/', BulkUpdateEffortScoreView.as_view(), name='bulk-update-effort'),
    path('bulk-update-marathon-time/', BulkUpdateMarathonTimeView.as_view(), name='bulk-update-marathon-time'),
]
