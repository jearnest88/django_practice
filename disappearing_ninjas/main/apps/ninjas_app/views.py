from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')

def ninja(request, color=None):
    ninja = 'img/Ninjas/'
    if not color:
        ninja += 'tmnt.png'
    elif color.lower() == 'blue':
        ninja += 'leonardo.jpg'
    elif color.lower() == 'red':
        ninja += 'raphael.jpg'
    elif color.lower() == 'orange':
        ninja += 'michelangelo.jpg'
    elif color.lower() == 'purple':
        ninja += 'donatello.jpg'
    else:
        ninja += 'notapril.jpg'

    context = {
        'ninja': ninja
    }
    return render(request, 'index.html', context)
#
# def ninja(request, color):
#     context = {
#     "blue": blue
#     "red": red
#     "orange": orange
#     "purple": purple
#     }


# Create your views here.
