from rest_framework.serializers import ModelSerializer

from profesor.models import Profesor


class ProfesorSerializer(ModelSerializer):

    class Meta:
        model = Profesor
        fields = '__all__'


class CrearProfesorSerializer(ModelSerializer):

    class Meta:
        model = Profesor
        fields = '__all__'
