from rest_framework.viewsets import ModelViewSet

from instituciones.models import Institucion
from instituciones.serializers import InstitucionesSerializer


class InstitucionesViewSet(ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionesSerializer
