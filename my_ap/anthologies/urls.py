from django.conf.urls import patterns, url


from anthologies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
    url(r'^(?P<book_id>\d+)/$', views.bookdetails, name='bookdetails'),
)
