from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^register$', views.register),
url(r'^login$', views.login),
url(r'^books/homepage$', views.homepage),
url(r'^books/new$', views.new),
url(r'^books/add$', views.add)
]
