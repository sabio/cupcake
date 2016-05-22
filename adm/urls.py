from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.GaleriaListView.as_view(), name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
	url(r'^addgaleria/$', views.addgaleria, name='addgaleria'),
	url(r'^editgaleria/(?P<galeria_id>[0-9]+)/$', views.editgaleria, name='editgaleria'),
	url(r'^descargaImagen/(?P<archivo_id>[0-9]+)/$', views.descargaImagen, name='descargaImagen'),
]


