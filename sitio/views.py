from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from sitio.forms.forms import ContactForm
from utils.utils import envia_email
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from models import Archivo, Galeria
import base64



prefijoTemplate = "sitio/"

def index(request):
    # return HttpResponse('Hello from Python!')
    galerias = Galeria.objects.all()
    imagenesID = Archivo.objects.values('id').order_by('galeria')
    return render(request, prefijoTemplate+'index.html',{'form':ContactForm(), 'imagenesID': imagenesID, 'galerias': galerias })


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


def descargaImagen(request, archivo_id):
	archivo = get_object_or_404(Archivo, pk=archivo_id)
	image_data = base64.decodestring(archivo.data)
	return HttpResponse(image_data, content_type=archivo.mimetype)