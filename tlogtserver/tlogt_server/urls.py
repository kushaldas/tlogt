from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'tlogt_server.views.dashboard', name='dashboard'),
)
