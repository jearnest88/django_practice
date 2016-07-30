from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^books$', views.index),
url(r'^books/(?P<id>\d+)$', views.show_review),
url(r'^books/add_review/(?P<id>\d+)$', views.add_review),
url(r'^books/new$', views.new),
url(r'^books/add$', views.add_book),
url(r'^books/destroy/(?P<id>\d+)$', views.destroy)
]
