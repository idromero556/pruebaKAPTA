from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.listarEmpresas, name='index'),
    path('usuario/registro/', views.agregarUsuarioview, name="agregarUsuario"),
    path('registroUsuario/', views.agregarUsuario, name = "registroUsuario"),
    path('login/', views.loginView, name='login'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutView, name='logout'),
    path('isLogged/', views.isLoggedView, name='isLogged'),
    path('listarProyectos/', views.consultarProyectos, name='listarProyectos'),
    url(r'^verListasTareas/(?P<pk>\d+)/$', views.consultarTareas, name='verListasTareas'),
    url(r'^listarServicios/(?P<pk>\d+)/$', views.listarServicios, name='listarServicios'),
    url(r'^listarMercados/(?P<pk>\d+)/$', views.listarMercados, name='listarMercados'),
    url(r'^crearServicio/(?P<pk>\d+)/$', views.crearServicio, name='crearServicio'),
    url(r'^crearServicioForm/(?P<pk>\d+)/$', views.crearServicioForm, name='crearServicioForm'),
    url(r'^agregarMercado/(?P<pk>\d+)/$', views.agregarMercado, name='agregarMercado'),
    url(r'^agregarMercadoForm/(?P<pk>\d+)/$', views.agregarMercadoForm, name='agregarMercadoForm'),
    url(r'^listarProyectosM/(?P<pk>\d+)/$', views.listarProyectos, name='listarProyectosM'),
    url(r'^listarTareas/(?P<pk>\d+)/$', views.listarTareas, name='listarTareas'),
    url(r'^agregarTarea/(?P<pk>\d+)/$', views.agregarTarea, name='agregarTarea'),
    url(r'^agregarTareaForm/(?P<pk>\d+)/$', views.agregarTareaForm, name='agregarTareaForm'),
    ]
