from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        if('count' in request.session) == False:
            request.session['count'] = 1
        else:
            request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
# Create your views here.
def result(request):
    return render(request, 'result.html')
