from django.shortcuts import render, redirect, HttpResponse
import random
from django.contrib import messages

def index (request):
    if('count' in request.session) == False:
        request.session['count'] = 0
    else:
            request.session['count']
    return render(request, 'index.html')

# Create your views here.
def process(request):
        name = request.POST['action']
        if request.method == 'POST':
            if name == 'hidden_farm':
                gold_gen = random.randint(10,20)
                request.session['count'] += gold_gen
                messages.info(request, 'Found ' + str(gold_gen) + " gold!")
            if name == 'hidden_cave':
                gold_gen = random.randint(5,10)
                request.session['count'] += gold_gen
                messages.info(request, 'Found ' + str(gold_gen) + " gold!")
            if name == 'hidden_house':
                gold_gen = random.randint(2,5)
                request.session['count'] += gold_gen
                messages.info(request, 'Found ' + str(gold_gen) + " gold!")
            if name == 'hidden_casino':
                gold_gen = random.randint(0,50)
                request.session['count'] += gold_gen
                messages.info(request, 'Found ' + str(gold_gen) + " gold!")

        return redirect('/')

def reset(request):
    if request.method == 'POST':
        try:
            del request.session['count']
        except:
            pass
        return redirect('/')
    else:
        return redirect('/')
