from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html'),
            # is it possible to set extra variables for the template here
        name='poll_index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html'),
        name='poll_detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^(?P<poll_id>\d+)/suggest_choice/$', 'polls.views.suggest_choice'),
    url(r'^(?P<poll_id>\d+)/process_suggest_choice/$', 'polls.views.process_suggest_choice'),
    url(r'^search', 'polls.views.search'),
    url(r'^random$', 'polls.views.random'),
    url(r'^add_poll$', 'polls.views.add_edit_poll'),
    #TODO: when an id is called load edit poll
)