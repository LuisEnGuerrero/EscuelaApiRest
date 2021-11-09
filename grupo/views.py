from rest_framework.viewsets import ModelViewSet

from grupo.models import Grupo
from grupo.serializers import GrupoSerializer


class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
