from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.db.models import Q
from polls.models import Choice, Poll
from forms import PollForm
from django.utils import timezone


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to stop users double posting
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))


def suggest_choice(request, poll_id):
    #TODO: add choice handling here
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/suggest_choice.html', {'poll': p}, context_instance=RequestContext(request))

def add_edit_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            #TODO: have pub_date set automatically
            p = Poll(question=form.cleaned_data['question'], pub_date=timezone.now())
            p.save()
            return HttpResponseRedirect(reverse('poll_detail', args=(p.id,)))
    else:
        form = PollForm()
    return render_to_response('polls/add_edit_poll.html', {'form': form}, context_instance=RequestContext(request))


# Validate the choice and error if not appropriate, should this be called process_suggest_choice
def process_suggest_choice(request, poll_id):
    #TODO: research Django forms!
    #TODO: Validate the information (no duplicates) is this preventing againsts SQL injection?
    #TODO: Show the form again if not valid
    #TODO: set succcess message
    p = get_object_or_404(Poll, pk=poll_id)
    p.choice_set.create(choice_text=request.POST['choice'], votes=0)
    return HttpResponseRedirect(reverse('poll_detail', args=(p.id,)))

def search(request):
    query = request.GET.get('q', '')
    if query:
        #print 'got query' # prints to console is development setup
        qset = (
            Q(question__icontains=query) |
            Q(choice__choice_text__icontains=query)
        )
        results = Poll.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('polls/search.html', {"results": results, "query": query}, context_instance=RequestContext(request))


def random(request):
    # select a random poll
    p = Poll.objects.order_by('?')[0]
    # redirect to voting page for that poll id
    #print 'test' + (str)p.id
    return HttpResponseRedirect(reverse('poll_detail', args=(p.id,)))

