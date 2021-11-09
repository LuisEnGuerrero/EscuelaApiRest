from django.contrib import admin

# Register your models here.
from grupo.models import Grupo


class GrupoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "grado")
    search_fields = ("nombre", "grado")

admin.site.register(Grupo, GrupoAdmin)