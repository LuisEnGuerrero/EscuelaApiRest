from django.contrib import admin

# Register your models here.
from estudiante.models import Estudiante


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "institucion", "grupo")
    search_fields = ("nombres", "apellidos", "grupo")

admin.site.register(Estudiante, EstudianteAdmin)