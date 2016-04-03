from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# the YoutubeToken
class YoutubeToken(models.Model):
	userid = models.TextField()
	access_token = models.TextField()
	created_date = models.DateTimeField('date created', default=timezone.now)

	def __str__(self):
		return self.userid

# the File class
class DropboxFiles(models.Model):
	userid = models.ForeignKey(YoutubeToken, on_delete=models.CASCADE)
	name = models.TextField()
	link = models.TextField()
	size = models.BigIntegerField()
	uploaded = models.BooleanField(default=False)
	created_date = models.DateTimeField('date created', default=timezone.now)

	def __str__(self):
		return self.name
