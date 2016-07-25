from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Comment

def index(request):
    context = {
    "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    if request.method == 'GET':
        course = Course.objects.get(id=id)
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request, 'destroy.html', context)

    elif request.method == 'POST':
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('/')

def comment(request, id):
    if request.method == 'GET':
        context = {
            "course": Course.objects.get(id=id)
        }
        return render(request, 'comment.html', context)
    elif request.method == 'POST':
        course = Course.objects.get(id=id)
        Comment.objects.create(course=course, comment=request.POST['comment'])
        return redirect('/comment/{}'.format(id))
