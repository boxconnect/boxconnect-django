from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

def index(request):
	return render(request, 'youtube/base.html')

def save_dropbox_files(request):
	request.session["files"] = json.loads(request.POST.get('files'))
	# explicitley tell django that we modified the session variables
	request.session.modified = True
	return JsonResponse({'success': True, 'bc_token': request.session.session_key})