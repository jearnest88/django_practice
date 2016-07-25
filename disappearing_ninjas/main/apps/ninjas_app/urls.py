from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'ninja/$', views.ninja),
url(r'ninja/(?P<color>\w+)/$', views.ninja)
]
