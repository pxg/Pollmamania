from contact.models import Contact
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')

            # Save to DB are explict field names requied/good practice?
            c = Contact(topic=topic, message=message, sender=sender)
            c.save()

            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['petegraham1@gmail.com']
            )
            #TODO: could we set a message on the original form (or send ajax and not page reload?
            return HttpResponseRedirect(reverse('contact.views.thanks'))
    else:
        form = ContactForm(initial={'sender': 'user@example.com'})
    return render_to_response('contact/index.html', {'form': form}, context_instance=RequestContext(request))


def thanks(request):
    return render_to_response('contact/thanks.html', {}, context_instance=RequestContext(request))