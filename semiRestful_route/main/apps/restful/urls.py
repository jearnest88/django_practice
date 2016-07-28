from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^product$', views.index),
url(r'^product/new$', views.new),
url(r'^product/create$', views.create),
url(r'^product/delete/(?P<id>\d+)$', views.delete),
url(r'^product/show/(?P<id>\d+)$', views.show),
url(r'^product/edit/(?P<id>\d+)$', views.edit),
url(r'^product/change/(?P<id>\d+)$', views.change)

]
