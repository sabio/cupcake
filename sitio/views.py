from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from sitio.forms.forms import ContactForm, NuevaGaleriaForm
from sitio.models import Galeria, Archivo
from utils.utils import envia_email

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from datetime import datetime   


prefijoTemplate = "sitio/"

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, prefijoTemplate+'index.html',{'form':ContactForm()})


def envioContacto(request):	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		print "form.is_valid() = %s" % form.is_valid()
		print "request.is_ajax() = %s" % request.is_ajax()
		if form.is_valid():
			#envia_email("Mensaje desde el portal web", [form.cleaned_data['email']], form.cleaned_data['comentarios'])
			response_data = {}
			response_data['result'] = 'OK'
			return JsonResponse(response_data)
	else:
		form = ContactForm()

	# return render(request, prefijoTemplate+'index.html', {'form': form})


def login(request):
	if request.method == 'GET':
		return render(request, prefijoTemplate+'login.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(username=username, password=password)
		print "user = %s" % user
		auth_login(request, user)

	return render(request, prefijoTemplate+'login.html')


def logout(request):
	auth_logout(request)
	return redirect('/login/')
	# return render(request, prefijoTemplate+'login.html')




def nuevagaleria(request):
	if request.method == 'GET':
		imgs = Archivo.objects.all()
		print imgs
		return render(request, prefijoTemplate+'nuevagaleria.html',{'form':NuevaGaleriaForm(), 'imgs':imgs})
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
		archivo.mimetype = "sdf"
		archivo.extension = "sdf"
		archivo.save()

		return render(request, prefijoTemplate+'nuevagaleria.html',{'form':NuevaGaleriaForm()})

