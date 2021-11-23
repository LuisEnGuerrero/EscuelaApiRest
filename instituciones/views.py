from rest_framework.viewsets import ModelViewSet

from instituciones.models import Institucion
from instituciones.serializers import InstitucionSerializer, CrearInstitucionSerializer, DetalleInstitucionSerializer
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly
)

class InstitucionesViewSet(ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset


    def get_serializer_class(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return InstitucionSerializer

        if self.request.method == 'POST':
            return CrearInstitucionSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleInstitucionSerializer

        return DetalleInstitucionSerializer



