from django import template
from sitio.models import Archivo

register = template.Library()



@register.simple_tag
def getCantDeImagenes(value): 
    return Archivo.objects.filter(galeria=value).count()


