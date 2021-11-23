from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_authenticated and request.user.is_staff:
            return True

        if request.user.is_authenticated and not request.user.is_staff and request.method == 'GET':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE', 'PATCH', 'PUT'] and obj.creado_por == request.user:
            return True

        return False

