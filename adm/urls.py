from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^adm/', views.adm, name='adm'),

        # url(r'^nuevagaleria/', sitio.views.nuevagaleria, name='nuevagaleria'),
        # url(r'^descargaImagen/(?P<archivo_id>[0-9]+)/$', sitio.views.descargaImagen, name='descargaImagen'),
]


