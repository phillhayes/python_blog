from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
url(r'^$', views.categories),
url(r'(?P<pk>\d+)/$', views.category_detail),
   
]