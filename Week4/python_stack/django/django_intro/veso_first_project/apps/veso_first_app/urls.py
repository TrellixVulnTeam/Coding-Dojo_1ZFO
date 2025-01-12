from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^bears/(?P<my_val>\d+)$', views.another_method),
  url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),
  url(r'^(?P<id>[0-9]+)/(?P<color>\w+)/(?P<bumbum>\w+)$', views.one_more)
]