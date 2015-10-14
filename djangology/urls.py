from django.conf.urls import patterns, include
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# Yu add 09/16
#import reporting

admin.autodiscover()
# Yu add 09/17


urlpatterns = patterns('',
    # Example:
    # Uncomment the next line to enable the admin:
    (r'^admin/c/', include('django.contrib.admindocs.urls')),
    
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/$', include('django.contrib.admindocs.urls')),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './dj/media/'}),  
                       #include all dj urls
    (r'^', include('dj.urls')),
                       # (r'^reporting/',include('reporting.urls')),

)

