from __future__ import unicode_literals
from django.db import models

  # Create your models here.
class Users(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      email_address = models.CharField(max_length=255)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
      title = models.CharField(max_length=255)
      message = models.TextField(max_length=1000)
      user_id = models.ForeignKey(User)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
      comment = models.TextField(max_length=1000)
      user_id = models.ForeignKey(User)
      message_id = models.ForeignKey(Message)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
