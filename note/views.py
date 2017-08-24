
# -*- coding: utf-8 -*-
from note.models import Persona
from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from note.forms import forma, NuevaCarpeta, NuevaNota, BookForm
from note.appsfunciones  import DropNote
import os, sys
#encoding= utf-8
def inicial(request):
	if not request.user.is_anonymous():
		n=True

	return render_to_response("note/indice.html",locals(),context_instance=RequestContext(request))

#Logueo del usuario registrado
def login(request):

	if not request.user.is_anonymous():
		return HttpResponseRedirect('')		

	if request.method=='POST':
		form = AuthenticationForm(request.POST)

		if form.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
		
			user = authenticate(username=username, password=clave)

			if user is not None:
				if user.is_active:
					auth_login(request, user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/')
			else:
					return HttpResponseRedirect('/')
	else:
		form= AuthenticationForm()

	return render_to_response('note/login.html', locals(), context_instance=RequestContext(request))

#Registro del nuevo usuario
def nuevoUser(request):

	if request.method == 'POST':


		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			npersona=Persona(user=username, token="indefinido", nombre="indefinido", edad=0)
			npersona.save()
			form.save()
			
			return HttpResponseRedirect('/entrar')
	else:
		form=UserCreationForm()
	return render_to_response('note/usuario.html', locals(), context_instance=RequestContext(request))


def cerrar(request):
	logout(request)
	return render_to_response('note/indice.html', context_instance=RequestContext(request))


#Modificacion de los datos del usuario
def crear(request):
	usuarios = request.user
#Clase DropNote sin token definido
	a=DropNote("")

	url=a.devolverURL()

	if not request.user.is_anonymous():
		n=True
		usuari = str(usuarios)
		ad=Persona.objects.get(user=usuari)
         
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	if request.method=='POST':
 
		form = forma(request.POST, request.FILES)
 
		if form.is_valid():

			tok = request.POST['token']
			nom = request.POST['nombre']
			age = request.POST['edad']
			ec=Persona.objects.get(user=usuarios)
			
			access_token=a.connect(tok) 

			ec.token=access_token
			ec.nombre=nom
			ec.edad=age
			ec.save()
             
			return HttpResponseRedirect('/')
	else:
		form = forma()
 
	return render_to_response('note/crear.html', locals(), context_instance=RequestContext(request))


#Perfil con los datos del usuario
def mostrar(request):

	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)

		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)


	return render_to_response('note/mostrar.html', locals(), context_instance=RequestContext(request))

#Visualizar y crear Carpetas
def carpeta(request):

	form = NuevaCarpeta()
	
	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
	
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)
	#Si no tienen guardado un token no podran acceder
	if not nombre.token=='indefinido':
	
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/crea')
	
	
	a=DropNote(nombre.token)
	
	lista = a.list_folder()
	
	
	if request.method=='POST':
	
		form = NuevaCarpeta(request.POST)
	
		if form.is_valid():
	
			cd = form.cleaned_data
			nombrecarpeta = cd.get('nombrecarpeta')
			lista=["á".encode('utf-8'),"é".encode('utf-8'),"í".encode('utf-8'),"ó".encode('utf-8'),"ú".encode('utf-8'),"ñ".encode('utf-8'), "Á".encode('utf-8'),"É".encode('utf-8'),"Í".encode('utf-8'),"Ó".encode('utf-8'),"Ú".encode('utf-8'),"Ñ".encode('utf-8')]
			error=False
			var=nombrecarpeta
			
			for x in var:
				print(x.encode('utf-8'))
				if x.encode('utf-8') in lista:
					error=True
	
			if(error==False):
	
				crearcarpeta = a.crearcarpeta(nombrecarpeta)
				return HttpResponseRedirect('/carpeta')
	                
			else:
				return HttpResponseRedirect('/carpeta')
	
	else:
		form = NuevaCarpeta()
	
	
	listaF=[]
	for a in lista:
		b=a.split("/")
		listaF.append(b[1])
	
	return render_to_response('note/carpeta.html', locals(), context_instance=RequestContext(request))


#Listado de carpetas existentes
def crearnota(request):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	if not nombre.token=='indefinido':

		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/crea')

	a=DropNote(nombre.token)

	lista = a.list_folder()

	listaF=[]
	for a in lista:
		b=a.split("/")
		listaF.append(b[1])


	return render_to_response('note/crearnota.html', locals(), context_instance=RequestContext(request))

#Creacion de nuevas notas
def crearnotnombre(request, ruta):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)


	a=DropNote(nombre.token)

	lista = a.list_folder()

	if request.method=='POST':
 
		form = NuevaNota(request.POST)

		if form.is_valid():

			cd = form.cleaned_data
			nota = cd.get('nota')

			lista=["á".encode('utf-8'),"é".encode('utf-8'),"í".encode('utf-8'),"ó".encode('utf-8'),"ú".encode('utf-8'),"ñ".encode('utf-8'), "Á".encode('utf-8'),"É".encode('utf-8'),"Í".encode('utf-8'),"Ó".encode('utf-8'),"Ú".encode('utf-8'),"Ñ".encode('utf-8')]
			error=False
			var=nota
			
			for x in var:
				print(x.encode('utf-8'))
				if x.encode('utf-8') in lista:
					error=True

			if(error==False):
				
				nuevanota = a.crearnota(nota, ruta)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/crearnotnombre/ruta')


	else:
		form = NuevaNota()

	return render_to_response('note/crearnotnombre.html', locals(), context_instance=RequestContext(request))


#Borrado de carpetas
def borrarcarpeta(request, ruta):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	a=DropNote(nombre.token)

	borrarcarpeta = a.borrarcarpeta(ruta)


	return render_to_response('note/borrarcarpeta.html', locals(), context_instance=RequestContext(request))

# Listar todas las carpetas
def listarcarpetaN(request):

	form = NuevaCarpeta()

	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)

		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	if not nombre.token=='indefinido':

		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/crea')

	a=DropNote(nombre.token)

	lista = a.list_folder()

	listaF=[]
	for a in lista:
		b=a.split("/")
		listaF.append(b[1])


	if request.method=='POST':
 
		form = NuevaCarpeta(request.POST)
 
		if form.is_valid():

			cd = form.cleaned_data
			nombrecarpeta = cd.get('nombrecarpeta')
			crearcarpeta = a.crearcarpeta(nombrecarpeta)
			return HttpResponseRedirect('/')
	else:
		form = NuevaCarpeta()
	
	return render_to_response('note/vernotas1.html', locals(), context_instance=RequestContext(request))

#Listar todas las notas
def listarnota(request, ruta):

	usuarios = str(request.user)
	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)

		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	a=DropNote(nombre.token)

	lista = a.listarnotas(ruta)
#Para seleccionar solo el nombre de la nota
	listaF=[]
	nombruta=[]
	for a in lista:
		b=a.split("/")
		listaF.append(b[2])
	
	
	return render_to_response('note/vernotas2.html', locals(), context_instance=RequestContext(request))

#Borrado de notas
def borrarnota(request, ruta, nomb):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	a=DropNote(nombre.token)

	borrarnota = a.borrarnota(ruta, nomb)


	return render_to_response('note/borrarnota.html', locals(), context_instance=RequestContext(request))

#Lectura de notas
def leernota(request, ruta, nomb):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')
	nombre=Persona.objects.get(user=usuarios)

	a=DropNote(nombre.token)

	leer= a.leernota(ruta, nomb)

	return render_to_response('note/leernota.html', locals(), context_instance=RequestContext(request))

#Edicion de notas
def editarnota(request, ruta, nomb):

	usuarios = str(request.user)

	if not request.user.is_anonymous():
		ad=Persona.objects.get(user=usuarios)
		
		n=True
		
	else:
		n=False
	if n==False:
		return HttpResponseRedirect('/entrar')

	nombre=Persona.objects.get(user=usuarios)
	a=DropNote(nombre.token)
	leer= a.leernota(ruta, nomb) 

	data = {'text': leer} 

	if request.method == 'POST':

		form = BookForm(request.POST)
		if form.is_valid():
#guardamos el texto con encode para dejarnos poner simbolos y tildes
			texto=request.POST['text'].encode('utf-8')
			a.modificarnota(texto,"/"+ruta+"/"+nomb)
			
	else: 
		form=BookForm(data)

	return render_to_response('note/editarnota.html', locals(), context_instance=RequestContext(request))
