from rest_framework.viewsets import ModelViewSet

from tareas.models import Tarea
from tareas.serializers import TareasSerializer


class TareasViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareasSerializer
