from django.core.mail import send_mail
from .models import DropboxYouTube

def get_token(backend, user, response, *args, **kwargs):

	social = user.social_auth.get(provider='google-oauth2')
	token = social.extra_data['access_token']

	bc = DropboxYouTube(userid=response["id"], access_token=token)
	bc.save()
