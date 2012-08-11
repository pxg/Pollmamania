from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')

            print 'about to send mail'
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['petegraham1@gmail.com']
            )
            # could we set a message on the original form (or send ajax and not page reload?
            return HttpResponseRedirect('/contact/thanks/')
            #TODO: add a reverse lookup for the url like reverse('poll_detail', args=(p.id,)))
    else:
        form = ContactForm(initial={'sender': 'user@example.com'})
    return render_to_response('contact/index.html', {'form': form}, context_instance=RequestContext(request))