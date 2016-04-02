from django.core.mail import send_mail

def send_debug(backend, user, response, *args, **kwargs):
	send_mail('Debug from Django', vars(kwargs), 'django@heroku.com', ['jan.moehrke@googlemail.com'], fail_silently=False)