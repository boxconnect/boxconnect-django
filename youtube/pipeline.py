from django.core.mail import send_mail
from .models import YoutubeToken

def get_token(backend, user, response, *args, **kwargs):

	social = user.social_auth.get(provider='google-oauth2')
	token = social.extra_data['access_token']
	print "Backend: ", backend

	try:
		bc = YoutubeToken(userid=response["id"], access_token=token)v
		bc.save()
	except:
		print "CONNECTION COULD NOT BE SAVED."
