from django.core.mail import send_mail

def send_debug(backend, user, response, *args, **kwargs):
	print response
	#send_mail('Debug from Django', response, 'django@heroku.com', ['jan.moehrke@googlemail.com'], fail_silently=False)
