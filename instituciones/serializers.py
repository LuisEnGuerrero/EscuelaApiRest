from rest_framework.serializers import ModelSerializer

from instituciones.models import Institucion


class InstitucionesSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__al__'

