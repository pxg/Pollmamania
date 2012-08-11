from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #TODO: move contact urls to their own file
    url(r'^feedback$', 'contact.views.index'),
    url(r'^feedback/thanks', 'contact.views.thanks'),
)