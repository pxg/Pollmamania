from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll

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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))


def suggest_choice(request, poll_id):
    #TODO: add choice handling here
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/suggest_choice.html', {'poll': p}, context_instance=RequestContext(request))


# Validate the choice and error if not appropriate, should this be called process_suggest_choice
def process_suggest_choice(request, poll_id):
    # Validate the information
    # Show the form again if not valid
    # If valid then redirect and set succcess message
    p = get_object_or_404(Poll, pk=poll_id)
    p.choice_set.create(choice_text=request.POST['choice'], votes=0)
    return HttpResponseRedirect(reverse('poll_detail', args=(p.id,)))