from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	#print 'got here'
	return render_to_response('contact/index.html', {}, context_instance=RequestContext(request))