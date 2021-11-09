from django.contrib import admin

# Register your models here.
from clase.models import Clase


class ClaseAdmin(admin.ModelAdmin):
    list_display = ("nombre", "grupo")
    search_fields = ("nombre", "grupo")


admin.site.register(Clase, ClaseAdmin)
