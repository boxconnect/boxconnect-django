from django.core.mail import send_mail
from django.contrib.sessions.backends.db import SessionStore
from .models import YoutubeToken

def get_token(backend, user, response, *args, **kwargs):

	social = user.social_auth.get(provider='google-oauth2')
	token = social.extra_data['access_token']
	bc_token = backend.strategy.session_get('bc_token', None)
	print "Token: ", bc_token

	# get files formerly stored in the session
	session =  SessionStore(session_key=bc_token)
	files = session.get('files', {})
	print files
	
	try:
		bc = YoutubeToken(userid=response["id"], access_token=token)
		bc.save()
	except:
		print "CONNECTION COULD NOT BE SAVED."
