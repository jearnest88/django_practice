from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message, Comment

def index(request):
    User.objects.create(first_name="jeff", last_name="jeffrey", email_address="jeff@jeff.com", password="lol123")
    user = User.objects.all()
    print (user)
    return render(request, 'index.html')

# Create your views here.
