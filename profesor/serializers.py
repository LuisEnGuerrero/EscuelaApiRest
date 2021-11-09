from rest_framework.serializers import ModelSerializer

from profesor.models import Profesor


class ProfesoresSerializer(ModelSerializer):

    class Meta:
        model = Profesor
        fields = '__al__'

