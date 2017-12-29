from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.post, name='post'),
    url(r'b/(?P<pk>\w+)$', views.blog, name='blog'),
]
