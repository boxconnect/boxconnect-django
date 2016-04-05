from django.core.mail import send_mail
from django.contrib.sessions.backends.db import SessionStore
from .models import YoutubeToken, DropboxFile

def get_token(backend, user, response, *args, **kwargs):

	# get token from the oauth2 flow
	social = user.social_auth.get(provider='google-oauth2')
	token = social.extra_data['access_token']

	# get our session token (from the dropbox files)
	bc_token = backend.strategy.session_get('bc_token', None)

	# if the token can be obtained, get the files formerly stored in the session
	if bc_token:
		session = SessionStore(session_key=bc_token)
		files = session.get('files', {})

		try:
			youtube_token = YoutubeToken(userid=response["id"], access_token=token)
			youtube_token.save()

			for file in files:
				dbfile = DropboxFile(name=file["name"], link=file["link"], size=file["bytes"], userid=youtube_token)
				dbfile.save()
		except:
			print "CONNECTION COULD NOT BE SAVED."