from __future__ import unicode_literals

from django.db import models

# Create your models here.
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def email(self, email):
        if len(email) < 1:
            return (False, 'Please enter an email')
        elif not EMAIL_REGEX.match(email):
            return(False, 'Enter a valid email address')
        else:
            return(True, 'The email address you entered {} is a valid email address. Thank you!'.format(email))

class Email(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager= UserManager()
    objects = models.Manager()
