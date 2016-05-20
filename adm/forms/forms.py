# -*- encoding: utf-8 -*-
from django import forms
from django.forms.formsets import BaseFormSet




class ImagenForm(forms.Form):
	# imagen = forms.FileField(label='Imagen')
	imagen = forms.CharField(max_length=30,label='imagen')



class ImagenFormSet(BaseFormSet):
	"""
	def clean(self):
		super(ImagenFormSet, self).clean()

		if any(self.errors):
			return
		
		for form in self.forms:
			print "form.cleaned_data = %s" % form.cleaned_data
			if form.cleaned_data:
				imagen = form.cleaned_data['imagen']
				if not imagen:raise forms.ValidationError('Tiene que ingresar todas la imagenes',code='no_image')
"""




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
	
