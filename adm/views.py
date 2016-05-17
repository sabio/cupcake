# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from sitio.models import Galeria, Archivo
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def index(request):
	return HttpResponse('Hello from Python!')

def hola():
	return "HOLAAA"

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		print("usuario = {}".format(user))

		if user is not None and user.is_active:
			auth_login(request, user)
			print user.user_permissions
			return redirect('/adm/adm')
		else:
			return render(request, 'login.html',{'mensaje':'Usuario y/o contraseña incorrecto(s)'})


def adm(request):
	return render(request, 'adm.html',{'galeria_list': Galeria.objects.all()} )


def logout(request):
	auth_logout(request)
	return redirect('/adm/login/')




def nuevagaleria(request):
	if request.method == 'GET':
		imgs = Archivo.objects.all()
		print imgs
		return render(request, 'nuevagaleria.html',{'form':NuevaGaleriaForm(), 'imgs':imgs})
	elif request.method == 'POST':
		
		# print "titulo = %s" % request.POST['title']
		# print "archivo = %s" % request.POST['fileimg']

		galeria = Galeria()
		galeria.nombre = request.POST['title']
		galeria.fecha = datetime.now()
		galeria.save()

		archivo = Archivo()
		archivo.galeria = galeria
		archivo.imagen = request.FILES['fileimg']
		data = request.FILES['fileimg'].read()
		archivo.data = base64.encodestring(data)
		archivo.mimetype = "sdf"
		archivo.extension = "sdf"
		archivo.save()

		return render(request, 'nuevagaleria.html',{'form':NuevaGaleriaForm()})

"""
def descargaImagen(request, archivo_id):
	archivo = get_object_or_404(Archivo, pk=archivo_id)
	image_data = base64.decodestring(archivo.data)
	return HttpResponse(image_data, content_type="image/png")

	"""