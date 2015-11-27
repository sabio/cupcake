from django.core.mail import send_mail


def envia_email(titulo, destinatarios, mensaje):
	print "----------------------------l--------------"
	send_mail(titulo, mensaje, 'sabiocharro@gmail.com', destinatarios, fail_silently = False)