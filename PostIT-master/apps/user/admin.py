from django.contrib import admin
from apps.user.models import *

# Register your models here.


class notaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha")
    list_filter = (
        "fecha",
    )
    date_hierarchy = "fecha"


admin.site.register(nota, notaAdmin)
