from rest_framework.serializers import ModelSerializer

from materias.models import Materia


class MateriasSerializer(ModelSerializer):

    class Meta:
        model = Materia
        fields = '__al__'

