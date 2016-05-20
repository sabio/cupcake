from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from sitio.forms.forms import ContactForm
from utils.utils import envia_email
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from datetime import datetime   
import base64


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


