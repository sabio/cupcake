from django.core.mail import send_mail


def envia_email(titulo, destinatarios, mensaje):
	print "----------------------------l--------------"
	send_mail(titulo, mensaje, 'sabiocharro@gmail.com', destinatarios, fail_silently = False)



def get_extension_file(file):
	s = str(file)
	if s.find(".") == -1:
		return ""

	return s.split(".")[-1]

