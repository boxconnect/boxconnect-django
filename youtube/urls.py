from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^save_dropbox_files/$', views.save_dropbox_files, name='save_dropbox_files'),
	url(r'^$', views.index, name='index'),
]