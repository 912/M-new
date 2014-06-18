from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_ap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^anthologies/', 'anthologies.views.bookdetails', name='bookdetails'),
    url(r'^admin/', include(admin.site.urls)),
)