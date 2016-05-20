from __future__ import unicode_literals

from django.db import models



class Galeria (models.Model):
	nombre = models.CharField(max_length=50)
	fecha = models.DateField()

class Archivo (models.Model):
	galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
	mimetype = models.CharField(max_length=30)
	extension = models.CharField(max_length=30)
	imagen = models.ImageField(upload_to='imguploads')
	data = models.TextField(db_column='data',blank=True)


