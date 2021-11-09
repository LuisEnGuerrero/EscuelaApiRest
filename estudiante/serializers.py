from rest_framework.serializers import ModelSerializer

from estudiante.models import Estudiante


class EstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__al__'

