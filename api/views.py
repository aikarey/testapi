from django.shortcuts import render
from django.http import HttpResponse
from zippyshare_downloader import extract_info
import json



def index(request):
	response = json.dumps([{}])
	return HttpResponse(response, content_type="text/json")
# Create your views here.

def get_link(request, link):
	if request.method == "GET":
		link = link.replace('-', '/')
		file_info = extract_info(link, download=False)
		response = json.dumps([{'name': file_info.name, 'size': str(file_info.size/1000000) + " MB", 'download_url': file_info.download_url}])
		return HttpResponse(response, content_type="text/json")