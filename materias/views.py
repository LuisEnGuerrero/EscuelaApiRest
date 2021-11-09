from rest_framework.viewsets import ModelViewSet

from materias.models import Materia
from materias.serializers import MateriaSerializer


class MateriasViewSet(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
