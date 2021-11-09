from rest_framework.serializers import ModelSerializer

from clase.models import Clase


class ClaseSerializer(ModelSerializer):

    class Meta:
        model = Clase
        fields = '__all__'


class CrearClaseSerializer(ModelSerializer):

    class Meta:
        model = Clase
        fields = '__all__'
