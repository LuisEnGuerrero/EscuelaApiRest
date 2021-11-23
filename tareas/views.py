from copy import copy
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from estudiante.serializers import EstudianteSerializer
from tareas.models import Tarea
from tareas.permissions import CustomPermission
from tareas.serializers import TareaSerializer, CrearTareaSerializer, DetalleTareaSerializer
from tareas.tasks import send_email


class TareasViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = DetalleTareaSerializer
    permission_classes = (CustomPermission,)

    def get_serializer_class(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return TareaSerializer

        if self.request.method == 'POST':
            return CrearTareaSerializer

        if self.action == 'retrieve' and self.request.user.is_staff:
            return DetalleTareaSerializer

        return DetalleTareaSerializer


    def create(self, request, *args, **kwargs):
        data = copy(self.request.data)
        data['creada_por'] = self.request.user.id
        serializer_class = self.get_serializer_class()
        serialized = serializer_class(data=data)

        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(
            status=status.HTTP_201_CREATED,
            data=serialized.data
        )

    def get_queryset(self):
        try:
            data = {}
            for i in self.request.query_params:
                data[i] = self.request.query_params[i]
            return self.queryset.filter(**data)
        except Exception as e:
            return self.queryset


    @action(methods=['POST'], detail=True)
    def publicar(self, request, pk=None):
        tarea = self.get_object()
        tarea.entregada = False
        tarea.save()

        emails = []
        for estudiante in tarea.grupo.estudiantes.all():
            emails.append(estudiante.correo)

        send_email_datetime = datetime.now() + timedelta(minutes=2)
        send_email.apply_async(
            args=[emails, tarea.titulo],
            eto=send_email_datetime
        )

        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'POST'], detail=True)
    def estudiantes(self, request, pk=None):
        tarea = Tarea.objects.get(id=pk)
        if request.method == 'GET':
            estudiantes = tarea.grupo.estudiantes.all()
            serialized = EstudianteSerializer(estudiantes, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        if request.method == 'POST':
            return Response(
                #fala ta logica de negocio
                status=status.HTTP_200_OK
            )

    @action(methods=['GET'], detail=False)
    def order(self, request):
        order_by = '-id'
        if 'order_by' in self.request.query_params:
            order_by = self.request.query_params['order_by']

        queryset = self.get_queryset().order_by(order_by)
        serializer_class = self.get_serializer_class()
        serrialized = serializer_class(queryset, many=True)
        return Response (
            status=status.HTTP_200_OK,
            data=serrialized.data
        )
