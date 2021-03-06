"""cupcake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import settings 
import django.views.static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


import hello.views
import sitio.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', sitio.views.index, name='index'),
    url(r'^envioContacto$', sitio.views.envioContacto, name='envioContacto'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba$', hello.views.index, name='index2'),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
    
    url(r'^adm/', include('adm.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


