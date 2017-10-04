from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
        url(r'^$', views.inicial, name= 'inicial'),
	url(r'^persona/$', views.nuevoUser, name= 'nuevoUser'),
	url(r'^entrar/$', views.login, name= 'login'),
	url(r'^cerrar/$', views.cerrar, name= 'cerrar'),
	url(r'^crea/$', views.crear, name= 'crear'),
	url(r'^perfil/$', views.mostrar, name= 'mostrar'),
	url(r'^carpeta/$', views.carpeta, name= 'carpeta'),
	url(r'^crearnota/$', views.crearnota, name= 'crearnota'),
	url(r'^crearnotnombre/(?P<ruta>\w+)/', views.crearnotnombre, name= 'crearnotnombre'),
	url(r'^borrarcarpeta/(?P<ruta>\w+)/', views.borrarcarpeta, name= 'borrarcarpeta'),
	url(r'^listarcarpetaN/$', views.listarcarpetaN, name= 'listarcarpetaN'),
	url(r'^listarnota/(?P<ruta>\w+)/', views.listarnota, name= 'listarnota'),
	url(r'^borrarnota/(?P<ruta>\w+)/(?P<nomb>\w+)/', views.borrarnota, name= 'borrarnota'),
	url(r'^leernota/(?P<ruta>\w+)/(?P<nomb>\w+)/', views.leernota, name= 'leernota'),
	url(r'^editarnota/(?P<ruta>\w+)/(?P<nomb>\w+)/', views.editarnota, name= 'editarnota'),
    ]
