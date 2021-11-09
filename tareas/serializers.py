from rest_framework.serializers import ModelSerializer

from tareas.models import Tarea


class TareasSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__al__'

