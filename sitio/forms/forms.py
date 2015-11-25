# -*- encoding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'id':'nombre', 'class': 'form-control', 'data-val':'true', 'placeholder':'Tu nombre'}))
    email = forms.CharField(label='Correo electrónico', max_length=100, widget=forms.TextInput(attrs={'id':'email', 'class': 'form-control', 'data-val':'true', 'placeholder':'Tu correo electrónico'}))
    comentarios = forms.CharField(label='Comentarios', max_length=1000, widget=forms.Textarea(attrs={'id':'comentarios', 'rows':'10', 'class':'form-control', 'cols':'30', 'placeholder':'Tu mensaje', 'style':'width: 100%' }))
