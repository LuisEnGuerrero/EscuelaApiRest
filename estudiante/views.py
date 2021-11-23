# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from estudiante.models import Estudiante
from estudiante.serializers import EstudianteSerializer
from estudiante.tasks import send_email

"""
class EstudianteGenericView(ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class EstudianteDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
"""


class EstudianteViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = IsAdminUser

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset


    @action(methods=['POST'], detail=True)
    def bienvenida(self, request, pk=None):
        estudiantes = self.get_object()

        emails = []
        for estudiante in estudiantes:
            emails.append(estudiante.correo)

        send_email_datetime = datetime.now() + timedelta(minutes=2)
        send_email.apply_async(
            args=[emails, estudiante.nombres+' '+estudiante.apellidos],
            eto=send_email_datetime
        )

        return Response(status=status.HTTP_200_OK)

"""
    def create(self, request, *args, **kwargs):
        # post
        pass
    
    def list(self, request, *args, **kwargs):
        # get
        pass
    
    def retrieve(self, request, *args, **kwargs):
        # get pk
        pass
    
    def destroy(self, request, *args, **kwargs):
        # delete
        pass
    
    def update(self, request, *args, **kwargs):
        # put / patch
        pass
"""