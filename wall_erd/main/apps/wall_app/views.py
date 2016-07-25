from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Posts

def index(request):
    People.objects.create(first_name="jeff", last_name="jeffrey", email_address="jeff@jeff.com")
    people = People.objects.all()
    print (people)
    return render(request, 'index.html')

# Create your views here.
