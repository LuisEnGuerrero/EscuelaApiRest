from rest_framework.viewsets import ModelViewSet

from grupo.models import Grupo
from grupo.serializers import GrupoSerializer


class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset

