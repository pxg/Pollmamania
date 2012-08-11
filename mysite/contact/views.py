from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

def index(request):
	print 'got here'
	return render_to_response('contact/index.html')