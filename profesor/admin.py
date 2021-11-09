from django.contrib import admin

# Register your models here.
from profesor.models import Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "institucion", "materia")
    search_fields = ("nombres", "apellidos", "materia")

admin.site.register(Profesor, ProfesorAdmin)