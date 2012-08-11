from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import ContactForm

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render_to_response('contact/index.html', {'form': form}, context_instance=RequestContext(request))