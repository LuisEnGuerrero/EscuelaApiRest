from rest_framework.serializers import ModelSerializer

from instituciones.models import Institucion

# get
class InstitucionSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__all__'

# post
class CrearInstitucionSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__all__'

# retrieve and admin
class DetalleInstitucionSerializer(ModelSerializer):

    class Meta:
        model = Institucion
        fields = '__all__'
