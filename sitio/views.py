from django.shortcuts import render


prefijoTemplate = "sitio/"

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, prefijoTemplate+'index.html')
