from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^process$', views.process),
url(r'^destroy/(?P<id>\d+)$', views.destroy),
url(r'^comment/(?P<id>\d+)$', views.comment)
]
