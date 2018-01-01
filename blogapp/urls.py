from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/(?P<pk>\d+)$', views.blog, name='blog'),
    url(r'^blog/(?P<pk>\d+)/follow/$', views.follow, name='follow'),

    url(r'^post/(?P<pk>\d+)$', views.post, name='post'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.delete_post, name='delete_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^post/(?P<pk>\d+)/read/$', views.read_post, name='read_post'),
]
