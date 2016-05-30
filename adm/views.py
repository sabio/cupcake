# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from sitio.models import Galeria, Archivo
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from mixins import LoginRequiredMixin
from forms.forms import NuevaGaleriaForm, ImagenFormSet, ImagenForm
from django.views.generic.edit import FormView
from django.forms.formsets import formset_factory
from datetime import datetime   
import base64
from utils.utils import get_extension_file
from django import forms
from django.contrib import messages



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
			return redirect('/adm/')
		else:
			return render(request, 'login.html',{'mensaje':'Usuario y/o contraseña incorrecto(s)'})


@login_required()
def logout(request):
	auth_logout(request)
	return redirect('/adm/login/')


# REVISAR ESTO PARA LA CUSTOM VALIDATION EN LAS FORMAS http://mikepk.com/2010/08/python-django-forms-errors-fieldsets/
# Y esto http://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html

@login_required()
def addgaleria(request):
	ImagenFormSet_obj = formset_factory(ImagenForm, formset=ImagenFormSet,extra=1)
	if request.method == 'GET':
		form = NuevaGaleriaForm()
		imagen_formset = ImagenFormSet_obj(initial=[])

		return render(request, 'galeriaForm.html',{'form':NuevaGaleriaForm(), 'imagen_formset':imagen_formset})
	if request.method == 'POST':
		form = NuevaGaleriaForm(request.POST)
		imagen_formset = ImagenFormSet_obj(request.POST, request.FILES)

		
		if form.is_valid() and imagen_formset.is_valid(): # Si la forma es valida
			
			if len(imagen_formset.forms) == 0: # Si no metieron ninguna forma de imagen
				form.add_error(None, "Ingrese al menos una imagen")
				return render(request, 'galeriaForm.html',{'form':form, 'imagen_formset':imagen_formset})

			galeria = Galeria()
			galeria.nombre = request.POST['title']
			galeria.fecha = datetime.now()
			galeria.save()
			
			for imagen_form in imagen_formset:
				imagen = imagen_form.cleaned_data.get('imagen')
				content_type = imagen.content_type
				extension = get_extension_file(imagen)

				archivo = Archivo()
				archivo.galeria = galeria
				data = imagen.read()
				archivo.data = base64.encodestring(data)
				archivo.mimetype = content_type
				archivo.extension = extension
				archivo.save()
			messages.success(request, 'Información correctamente guardada')
			return redirect('/adm/')

		return render(request, 'galeriaForm.html',{'form':form, 'imagen_formset':imagen_formset})






@login_required()
def deletegaleria(request, galeria_id):
	galeria = get_object_or_404(Galeria, pk=galeria_id)
	galeria.delete()
	messages.success(request, 'Se ha eliminado lo solicitado')
	return redirect('/adm/')


@login_required()
def editgaleria(request, galeria_id):
	galeria = get_object_or_404(Galeria, pk=galeria_id)
	imagenes = Archivo.objects.filter(galeria = galeria)

	ImagenFormSet_obj = formset_factory(ImagenForm, formset=ImagenFormSet,extra=1)
	

	if request.method == 'GET':
		form = NuevaGaleriaForm(initial={'title': galeria.nombre})
		imagen_formset = ImagenFormSet_obj(initial=[])


	if request.method == 'POST':
		form = NuevaGaleriaForm(request.POST)
		imagen_formset = ImagenFormSet_obj(request.POST, request.FILES)

		if form.is_valid() and imagen_formset.is_valid(): # Si la forma es valida
			

			galeria.nombre = request.POST['title']
			galeria.save()

			# Borramos las imagenes que se marcaron para borrar

			if request.POST['borrarFiles']:
				borrarFiles = request.POST['borrarFiles'].split(',')
				for idFile in borrarFiles:
					archivo = get_object_or_404(Archivo, pk=idFile)
					archivo.delete()


			
			for imagen_form in imagen_formset:
				imagen = imagen_form.cleaned_data.get('imagen')
				content_type = imagen.content_type
				extension = get_extension_file(imagen)

				archivo = Archivo()
				archivo.galeria = galeria
				data = imagen.read()
				archivo.data = base64.encodestring(data)
				archivo.mimetype = content_type
				archivo.extension = extension
				archivo.save()
			messages.success(request, 'Información correctamente guardada')	
			return redirect('/adm/')



	return render(request, 'galeriaForm.html',{'form':form, 'imagen_formset':imagen_formset, 'imagenes':imagenes})



# Vista del listado
class GaleriaListView(LoginRequiredMixin,ListView):
	model = Galeria
	template_name = 'galeriaList.html'
		






def descargaImagen(request, archivo_id):
	archivo = get_object_or_404(Archivo, pk=archivo_id)
	image_data = base64.decodestring(archivo.data)
	return HttpResponse(image_data, content_type=archivo.mimetype)

