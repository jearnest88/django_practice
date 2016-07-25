from django.shortcuts import render
from time import strftime, localtime
def index(request):
    time = {'time': strftime('%b %d, %Y %I: %M %p', localtime())}
    return render(request,'timedisplay/index.html', time)
