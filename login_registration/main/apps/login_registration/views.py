from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

#registration page
def index(request):
    request.session.flush()
    return render(request, 'index.html')

#process page to process registraion and login
def process(request, which_process):
    if request.method == 'POST':
        if which_process == 'register':
            result = User.userManager.register(request.POST)
            if result[0] == False:
                for error in result[1]:
                    messages.error(request, error)
                return redirect('/')
            else:
                request.session['name'] = request.POST['first_name']
                messages.success(request, result[1])
                return redirect('/success')

        else:
            result = User.userManager.login(request.POST)
            if result[0] == False:
                for error in result[1]:
                    messages.error(request, error)
                return redirect('/')
            else:
                messages.success(request, result[1])
                request.session['name'] = result[2]
                return redirect('/success')
    else:
        return redirect('/')
#sucessful login or registration
def success(request):
    return render(request, 'success.html')
