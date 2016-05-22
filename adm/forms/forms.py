# -*- encoding: utf-8 -*-
from django import forms
from django.forms.formsets import BaseFormSet




class ImagenForm(forms.Form):
	imagen = forms.FileField(label='imagen')
	# imagen = forms.CharField(max_length=30, label='imagen')



class ImagenFormSet(BaseFormSet):
	
	def clean(self):
		super(ImagenFormSet, self).clean()

		if any(self.errors):
			return
		
		""" ESTA VALIDACION LA PASAMOS AL VIEW
		if len(self.forms) == 0: # Si no metieron ninguna forma de imagen
			raise forms.ValidationError('Ingrese al menos una imagen',code='no_image')
		"""
		for form in self.forms:
			imagen = form.cleaned_data.get("imagen",None)
			if imagen == None: raise forms.ValidationError('Hace falta indicar una imagen',code='no_image')
	




class NuevaGaleriaForm(forms.Form):
	title = forms.CharField(max_length=30,label='Titulo')
	"""
	def __init__(self, *args, **kwargs):
		numImagenes = kwargs.pop('numImagenes')
		super(NuevaGaleriaForm, self).__init__(*args, **kwargs)
		# self.fields["title"].initial = "AAAAAAAAAAAAa"
		for i in range(0,numImagenes):
			self.fields["fileimg%d" % i] = forms.FileField(label='Imagen')
	"""
	
