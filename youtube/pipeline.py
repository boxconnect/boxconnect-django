from django.core.mail import send_mail

def get_token(backend, user, response, *args, **kwargs):
	social = user.social_auth.get(provider='google-oauth2')
	print "Token: ", social.extra_data['access_token']
