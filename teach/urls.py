from django.conf.urls import patterns, include, url
from lessons import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'lessons.views.front_page'),
    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'teach.views.logout_page'),
    (r'^profile/$', 'teach.views.profile'),
    (r'^profile/(\d+)$', 'teach.views.profile_individual'),
    (r'^profile/add$', 'teach.views.profile_create_or_update'),
    (r'^profile/(\d+)/edit$', 'teach.views.profile_create_or_update'),
    (r'^portal/$', include('portal.urls')),
    url(r'^lessons/', include('lessons.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
)
