from rest_framework.serializers import ModelSerializer

from materias.models import Materia


class MateriaSerializer(ModelSerializer):

    class Meta:
        model = Materia
        fields = '__all__'


class CrearMateriaSerializer(ModelSerializer):

    class Meta:
        model = Materia
        fields = '__all__'
