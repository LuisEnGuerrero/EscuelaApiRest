from rest_framework.serializers import ModelSerializer

from instituciones.models import Institucion


class InstitucionSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__all__'


class CrearInstitucionSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__all__'
