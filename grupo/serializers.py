from rest_framework.serializers import ModelSerializer

from grupo.models import Grupo


class GrupoSerializer(ModelSerializer):

    class Meta:
        model = Grupo
        fields = '__al__'

