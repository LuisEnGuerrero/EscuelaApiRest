from rest_framework.serializers import ModelSerializer

from tareas.models import Tarea

# get (list) and not admin
class TareaSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = ['titulo', 'entregada', 'fecha_vencimiento']

# post
class CrearTareaSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'

# retrieve and admin /
class DetalleTareaSerializer(ModelSerializer):

    class Meta:
        model = Tarea
        fields = '__all__'
