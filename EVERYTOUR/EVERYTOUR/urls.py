from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RETREAT.views.home', name='home'),
    # url(r'^QUIZ/', include('QUIZ.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tripinfo.views.login_user'),
    url(r'^login/$', 'tripinfo.views.login_user'),
    url(r'^home/$', 'tripinfo.views.index'),
    url(r'^registration/$', 'tripinfo.views.registration'),
    url(r'^statistics/$', 'tripinfo.views.statistics'),
    #url(r'^statistics_total/%', 'tripinfo.views.statistics'),
    url(r'^timetable/$', 'tripinfo.views.timetable'),
    url(r'^logout/$', 'tripinfo.views.logout_page'),
)
