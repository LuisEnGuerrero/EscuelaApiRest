from django.contrib import admin

# Register your models here.
from materias.models import Materia


class MateriasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "grado")
    search_fields = ("nombre", "grado")

admin.site.register(Materia, MateriasAdmin)