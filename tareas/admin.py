from django.contrib import admin

# Register your models here.
from tareas.models import Tarea

class TareasAdmin(admin.ModelAdmin):
    list_display = ("titulo", "materia", "fecha_vencimiento", "entregada", "calificacion")
    search_fields = ("titulo", "materia", "entregada")

admin.site.register(Tarea, TareasAdmin)