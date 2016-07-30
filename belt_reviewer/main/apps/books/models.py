from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
