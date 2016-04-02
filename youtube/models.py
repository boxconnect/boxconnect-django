from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DropboxYouTube(models.Model):
	access_token = models.CharField(max_length=250)
	#refresh_token = models.CharField(max_length=250)
	userid = models.CharField(max_length=100)

	def __str__(self):
		return self.userid