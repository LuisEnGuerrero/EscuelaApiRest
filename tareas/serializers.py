from rest_framework.serializers import ModelSerializer

from tareas.models import Tarea


class TareaSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'


class CrearTareaSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'
