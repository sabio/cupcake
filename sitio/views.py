from django.shortcuts import render
from sitio.forms.forms import ContactForm

prefijoTemplate = "sitio/"

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, prefijoTemplate+'index.html',{'form':ContactForm()})


def envioContacto(request):
	
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()

	return render(request, prefijoTemplate+'index.html', {'form': form})