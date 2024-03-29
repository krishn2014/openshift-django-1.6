from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# for including static sontent
import imp, os.path

site_media = os.path.join( os.path.dirname(__file__) , '../static' )

# @deprecated
# from django.views.generic.simple import direct_to_template
from django.shortcuts import render as direct_to_template

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mainapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Uncomment the next line to enable the admin
    url(r'^admin/', include(admin.site.urls)),

    # for static content. this is just for development
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': site_media }),
)
