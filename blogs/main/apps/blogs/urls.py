from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^$', views.index, name = 'index'),
url(r'^blogs$', views.blogs),
url(r'^comments/(?P<id>\d+)$', views.comments)
]
