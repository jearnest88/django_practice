from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
import re
import bcrypt

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def register(self, info):
        #register user
		first_name = str(info['first_name'])
		last_name = str(info['last_name'])
		email = info['email']
		password = info['password']
		confirm_pass = info['confirm_pass']
		errors = []
        #check if first name meets length and letter requirements
		if len(first_name) < 2:
			errors.append('First name needs to be longer...')
		elif str.isalpha(first_name) != True:
			errors.append('First name can only be letters...')
        #check if last name meets length and letter requirements
		if len(last_name) < 2:
			errors.append('Last name needs to be longer...')
		elif str.isalpha(last_name) != True:
			errors.append('Last name can only be letters...')
        #check if email is blank
		if len(email) < 1:
			errors.append('Email must be entered...')
		#check is email contains valid characters
		elif not EMAIL_REGEX.match(email):
			errors.append('Invalid Email Address...')
        #see is email already exists
		try:
			if User.objects.get(email=email):
				errors.append('Email is already registered...')
		except:
			pass
        #check if pw meets length requirements
		if len(password) < 8:
			errors.append('Password must be at least 8 characters...')
        #check if pws match
		elif password != confirm_pass:
			errors.append('Your passwords do not match...')

		if errors:
			return (False, errors)
        #encrypts pw
		else:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed)
			return (True, 'Successfully registered!')
    #attempt to login
	def login(self, info):
		errors = []
		email = info['email']
		password = info['password']
        #check if email matched email in DB
		try:
			user = User.objects.get(email=email)
			if bcrypt.hashpw(password.encode(), user.password.encode()) != user.password:
				errors.append('Wrong password...')
		except:
			errors.append('Email entered does not match any existing email...')

		if errors:
			return (False, errors)
		else:
			return (True, 'Successfully logged in!' , user.first_name)

#DB model
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()
