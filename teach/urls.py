from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teach.views.home', name='home'),
    # url(r'^teach/', include('teach.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Lessons (must be plural in url)
    url(r'^lessons/$', 'lessons.views.index'),
    url(r'^lessons/(?P<lesson_id>\d+)/$', 'lessons.views.detail'),

	# Promises
    url(r'^promises/$', 'lessons.views.promises'),
    url(r'^promises/(?P<promise_id>\d+)/$', 'lessons.views.promise_detail'),
    url(r'^promises/(?P<promise_id>\d+)/keep$', 'lessons.views.keep'),
    #url(r'^promise/(?P<promise_id>\d+)/status$', 'promise.views.status'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
