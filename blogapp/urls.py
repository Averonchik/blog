from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.post_list, name='post_list'),
    url(r'^p/\d+$', views.post, name='post'),
    url(r'b/\w+$', views.blog, name='blog'),
]
