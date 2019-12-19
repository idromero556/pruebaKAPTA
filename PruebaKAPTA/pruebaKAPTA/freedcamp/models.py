from django.db import models
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return 'Proyecto: '+self.nombre


class Tarea(models.Model):
    proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=200)
    estado=models.CharField(max_length=200)

    def __str__(self):
        return 'Tarea: '+self.nombre


class Empresa(models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return 'Empresa: '+self.nombre

class Servicio(models.Model):
    nombre=models.CharField(max_length=200)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Servicio: '+self.nombre

class Mercado(models.Model):
    nombre=models.CharField(max_length=200)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    proyectos = models.ManyToManyField(Proyecto, blank=True)

    def __str__(self):
        return 'Mercado: '+self.nombre
