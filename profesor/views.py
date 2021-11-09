from rest_framework.viewsets import ModelViewSet

from profesor.models import Profesor
from profesor.serializers import ProfesorSerializer


class ProfesoresViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
