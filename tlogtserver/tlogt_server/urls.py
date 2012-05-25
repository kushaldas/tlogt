from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(
            r'^$',
            'tlogt_server.views.dashboard',
            name='dashboard'
        ),
        url(
            r'^parser/(?P<parser_name>\w+)/$',
            'tlogt_server.views.parser_page',
            name='parser_page'
        ),
        url(
            r'^parser/(?P<parser_name>\w+)/(?P<index>\d+)/$',
            'tlogt_server.views.parser_page_on_specific_date',
            name='parser_page_on_specific_date'
        )
)
