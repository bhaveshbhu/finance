from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finance.views.home', name='home'),
    # url(r'^finance/', include('finance.foo.urls')),
    #url(r'^$', 'django.views.generic.simple.redirect_to',{'url': '/admin/'}),                   
    url(r'^dblayer/', include('dblayer.urls')),
    url(r'^utils/', include('utils.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
