from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clase.models import Clase
from clase.serializers import CrearClaseSerializer, ClaseSerializer


@api_view(http_method_names=['GET', 'POST'])
def clases(request):
    if request.method == 'POST':
        serialized = CrearClaseSerializer(data=request.data)
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

    if request.method == 'GET':
        clases = Clase.objects.all()
        serialized = ClaseSerializer(clases, many=True)
        return Response(data=serialized.data)


@api_view(http_method_names=['GET', 'DELETE', 'PUT', 'PATCH'])
def claseDetail(request, id):
    clase = get_object_or_404(Clase, id=id)

    if request.method == 'GET':
        serialized = ClaseSerializer(clase)
        return Response(data=serialized.data)

    if request.method == 'DELETE':
        clase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serialized = ClaseSerializer(clase, data=request.data)

        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    if request.method == 'PATCH':
        serialized = ClaseSerializer(
            clase,
            data=request.data,
            partial=True
        )

        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )
