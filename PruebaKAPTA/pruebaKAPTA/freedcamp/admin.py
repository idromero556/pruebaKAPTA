from django.contrib import admin
from .models import Mercado, Tarea, Proyecto, Servicio, Empresa

# Register your models here.
admin.site.register(Mercado)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Servicio)
admin.site.register(Empresa)
