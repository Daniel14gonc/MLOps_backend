# users/views.py
from rest_framework import generics, permissions
from .serializers import UserSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

User = get_user_model()

class BulkUpdateEffortScoreView(APIView):
    """
    Endpoint para actualizar el effort_score de múltiples usuarios.
    """
    def put(self, request):
        data = request.data  # Lista de objetos [{"id": 1, "effort_score": 85.5}, ...]

        # Validar que los datos sean una lista
        if not isinstance(data, list):
            return Response({"error": "Se espera una lista de objetos con 'id' y 'effort_score'."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Procesar las actualizaciones
        updated_users = []
        for record in data:
            user_id = record.get('id')
            effort_score = record.get('effort_score')

            if user_id is None or effort_score is None:
                return Response({"error": "Cada objeto debe incluir 'id' y 'effort_score'."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Actualizar el usuario correspondiente
            try:
                user = User.objects.get(id=user_id)
                user.effort_score = effort_score
                user.save()
                updated_users.append({"id": user_id, "effort_score": effort_score})
            except User.DoesNotExist:
                return Response({"error": f"Usuario con id {user_id} no encontrado."},
                                status=status.HTTP_404_NOT_FOUND)

        return Response({"updated_users": updated_users}, status=status.HTTP_200_OK)
    
class BulkUpdateMarathonTimeView(APIView):
    """
    Endpoint para actualizar el marathon time de múltiples usuarios.
    """
    def put(self, request):
        data = request.data  # Lista de objetos [{"id": 1, "marathon_time": 85.5}, ...]

        # Validar que los datos sean una lista
        if not isinstance(data, list):
            return Response({"error": "Se espera una lista de objetos con 'id' y 'marathon_time'."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Procesar las actualizaciones
        updated_users = []
        for record in data:
            user_id = record.get('id')
            marathon_time = record.get('marathon_time')

            if user_id is None or marathon_time is None:
                return Response({"error": "Cada objeto debe incluir 'id' y 'marathon_time'."},
                                status=status.HTTP_400_BAD_REQUEST)

            # Actualizar el usuario correspondiente
            try:
                user = User.objects.get(id=user_id)
                user.marathon_time = marathon_time
                user.save()
                updated_users.append({"id": user_id, "marathon_time": marathon_time})
            except User.DoesNotExist:
                return Response({"error": f"Usuario con id {user_id} no encontrado."},
                                status=status.HTTP_404_NOT_FOUND)

        return Response({"updated_users": updated_users}, status=status.HTTP_200_OK)