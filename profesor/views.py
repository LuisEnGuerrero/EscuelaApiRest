from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from profesor.models import Profesor
from profesor.serializers import ProfesorSerializer
from profesor.tasks import send_email



class ProfesoresViewSet(ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
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
        profesores = self.get_object()

        emails = []
        for profesor in profesores:
            emails.append(profesor.correo)

        send_email_datetime = datetime.now() + timedelta(minutes=2)
        send_email.apply_async(
            args=[emails, profesor.nombres+' '+profesor.apellidos],
            eto=send_email_datetime
        )

        return Response(status=status.HTTP_200_OK)

