from rest_framework.serializers import ModelSerializer

from estudiante.models import Estudiante


class EstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'


class CrearEstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'
