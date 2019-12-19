import json
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Empresa, Servicio, Mercado, Proyecto, Tarea


@csrf_exempt
def agregarUsuarioview(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        usuario = jsonUser['username']
        contrasena = jsonUser['password']

        user_model=User.objects.create_user(username=usuario, password= contrasena, last_login=timezone.now())
        #user_model.last_login = timezone.now() update_fields=['last_login']
        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def agregarUsuario(request):
    return render(request, "freedcamp/registro.html")


@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        password = jsonUser['password']
        email = jsonUser['username']
        user=authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            message="ok"
        else:
            message='El e-mail o la contraseña son inconrrectos'

    return JsonResponse({"message":message})


@csrf_exempt
def loginUser(request):
    return render(request, "freedcamp/login.html")


@csrf_exempt
def logoutView(request):
    logout(request)
    return JsonResponse({"message":'ok'})


@csrf_exempt
def isLoggedView(request):
    if request.user.is_authenticated:
        message = 'ok'
    else:
        message = 'no'
    return JsonResponse({"message": message})



@csrf_exempt
def listarEmpresas(request):

    if request.user.is_authenticated:
        listaEmpresas = Empresa.objects.all()

    else:
        listaEmpresas = ""
    return render(request, "freedcamp/index.html", {'empresas':listaEmpresas})


@csrf_exempt
def listarServicios(request,pk):
    empresa = get_object_or_404(Empresa, id=pk)
    servicios=Servicio.objects.filter(empresa=empresa).order_by('id')
    return render(request, "freedcamp/listarServicios.html", {'servicios': servicios, 'empresa':empresa})


@csrf_exempt
def listarMercados(request,pk):
    servicio = get_object_or_404(Servicio, id=pk)
    mercados=Mercado.objects.filter(servicio=servicio).order_by('id')
    return render(request, "freedcamp/listarMercados.html", {'mercados': mercados,'servicio':servicio})


@csrf_exempt
def crearServicio(request, pk):
    empresa = get_object_or_404(Empresa, id=pk)
    if request.method == 'POST':
        newServicio = Servicio(
            nombre=request.POST.get('nombre'),
            empresa=empresa,
        )
        newServicio.save()

    return HttpResponse(serializers.serialize("json", [newServicio]))


@csrf_exempt
def crearServicioForm(request, pk):
    empresa = get_object_or_404(Empresa, id=pk)
    return render(request, "freedcamp/servicioForm.html", {'empresa':empresa})


@csrf_exempt
def agregarMercado(request, pk):
    servicio = get_object_or_404(Servicio, id=pk)
    if request.method == 'POST':
        newMercado = Mercado(
            nombre=request.POST.get('nombre'),
            servicio=servicio,
        )
        newMercado.save()

    return HttpResponse(serializers.serialize("json", [newMercado]))

@csrf_exempt
def agregarMercadoForm(request,pk):
    servicio = get_object_or_404(Servicio, id=pk)
    return render(request, "freedcamp/mercadoForm.html", {'servicio':servicio})

@csrf_exempt
def listarProyectos(request,pk):
    mercado = get_object_or_404(Mercado, id=pk)
    proyectos=mercado.proyectos.all().order_by('id')
    return render(request, "freedcamp/listarProyectosM.html", {'proyectos': proyectos})

@csrf_exempt
def listarTareas(request,pk):
    proyecto = get_object_or_404(Proyecto, id=pk)
    tareas=Tarea.objects.filter(proyecto=proyecto).order_by('id')
    return render(request, "freedcamp/listarTareas.html", {'tareas': tareas, 'proyecto':proyecto})

@csrf_exempt
def agregarTarea(request, pk):
    proyecto = get_object_or_404(Proyecto, id=pk)
    if request.method == 'POST':
        newTarea = Tarea(
            proyecto=proyecto,
            nombre=request.POST.get('nombre'),
            estado='No Progress',
        )
        newTarea.save()

    return HttpResponse(serializers.serialize("json", [newTarea]))

@csrf_exempt
def agregarTareaForm(request,pk):
    proyecto = get_object_or_404(Proyecto, id=pk)
    return render(request, "freedcamp/tareaForm.html", {'proyecto':proyecto})



#Consulta de Freedcamp y almacenamiento en BD
@csrf_exempt
def consultarProyectos(request):

    def extraer(data):
        return {
            'id': data['project_id'],
            'name': data['project_name'],
        }


    proyectos = requests.get('https://freedcamp.com/api/v1/sessions/current?api_key='+settings.API_KEY).json()
    listaProyectos=list(extraer(p) for p in proyectos['data']['projects'])
    for p in listaProyectos:
        agregarProyecto(p['id'],p['name'])


    return render(request, "freedcamp/listarProyectos.html", {'proyectos': listaProyectos})


@csrf_exempt
def agregarProyecto(pk,nombre):
    newProyecto = Proyecto(
        pk=pk,
        nombre=nombre,
       )
    newProyecto.save()

    return HttpResponse(serializers.serialize("json", [newProyecto]))


@csrf_exempt
def consultarTareas(request, pk):

    def extraer(data):
        return {
            'id': data['id'],
            'name': data['title'],
            'project': data['project_id'],
            'status' : data['status_title']
        }

    tareas = requests.get('https://freedcamp.com/api/v1/tasks/?project_id='+pk+'&api_key='+settings.API_KEY).json()
    listasTareas=list(extraer(p) for p in tareas['data']['tasks'])
    for p in listasTareas:
        agregarTarea(p['id'],get_object_or_404(Proyecto,pk=p['project']),p['name'],p['status'])

    return render(request, 'freedcamp/listasTareas.html',{'listasTareas':listasTareas})

@csrf_exempt
def agregarTarea(pk,proyecto,nombre,estado):
    newTarea = Tarea(
        pk=pk,
        proyecto=proyecto,
        nombre=nombre,
        estado=estado,
       )
    newTarea.save()

    return HttpResponse(serializers.serialize("json", [newTarea]))
