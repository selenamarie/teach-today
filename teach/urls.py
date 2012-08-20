from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'teach.views.main_page'),
    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'teach.views.logout_page'),
	(r'^profile/$', 'teach.views.profile'),
    (r'^portal/$', include('portal.urls')),
	url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'', include('social_auth.urls')),
)
