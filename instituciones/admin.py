from django.contrib import admin

# Register your models here.
from instituciones.models import Institucion


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ("nombres", "ciudad", "pais")
    search_fields = ("nombres", "ciudad", "pais")


admin.site.register(Institucion, InstitucionAdmin)
