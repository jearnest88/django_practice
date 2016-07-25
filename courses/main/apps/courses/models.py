from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
# Create your models here.

class Comment(models.Model):
    course = models.ForeignKey(Course)
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
