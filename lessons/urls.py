from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('lessons.views',
	# Lessons (must be plural in url)
    url(r'^$', 'index'),
    url(r'^(?P<lesson_id>\d+)/$', 'detail'),
    url(r'^add/$', 'lesson_add'),
    url(r'^promises/$', 'promises'),
    url(r'^promises/add/$', 'promise_add'),
    url(r'^promises/(?P<promise_id>\d+)/$', 'promise_detail'),
    url(r'^promises/(?P<promise_id>\d+)/keep/$', 'do_assessment'),

    # Uncomment the next line to enable the admin:
)
