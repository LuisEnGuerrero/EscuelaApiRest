from rest_framework.viewsets import ModelViewSet

from materias.models import Materia
from materias.serializers import MateriaSerializer


class MateriasViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset

