from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from estudiante.models import Estudiante
from estudiante.serializers import EstudianteSerializer


class EstudianteGenericView(ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class EstudianteDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

