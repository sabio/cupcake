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
		imagen_formset = ImagenFormSet_obj(request.POST)

		for imagen_form in imagen_formset:
			print "valido = %s" %imagen_form.is_valid()
			imagen = imagen_form.cleaned_data.get('imagen')
			print "imagen = %s" % imagen

		if form.is_valid() and imagen_formset.is_valid(): # Si la forma es valida
			print "VALIDO!!!"
			return redirect('/adm/')

		return render(request, 'galeriaForm.html',{'form':form, 'imagen_formset':imagen_formset})	


		"""
		form = NuevaGaleriaForm(request.POST or None)
		if not form.is_valid():
			return render(request, 'galeriaForm.html',{'form':form})
		"""

		"""
		for a in form.fields:
			print "a = %s" % a

		print "file = %s" % request.FILES.get('fileimg0', False)
		print "file = %s" % request.FILES.get('fileimg1', False)
		"""

		"""	
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
		"""
		
		



@login_required()
def editgaleria(request, galeria_id):
	pass




# Vista del listado
class GaleriaListView(LoginRequiredMixin,ListView):
	model = Galeria
	template_name = 'galeriaList.html'
		





"""
def descargaImagen(request, archivo_id):
	archivo = get_object_or_404(Archivo, pk=archivo_id)
	image_data = base64.decodestring(archivo.data)
	return HttpResponse(image_data, content_type="image/png")

	"""


