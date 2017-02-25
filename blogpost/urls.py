from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^$', views.blogposts),
url(r'(?P<pk>\d+)/$', views.blogpost_detail),
   
]