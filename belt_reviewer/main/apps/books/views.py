from django.shortcuts import render, redirect, HttpResponse
from ..login_reg.models import User
from .models import Book, Review
from django.contrib import messages
import bcrypt

#main user login screen
def index(request):
    context = {
    "books": Book.objects.all()
    }
    return render(request,'books/index.html', context)

#sends user to a page to add a book
def new(request):
    return render(request, 'books/add.html')

#adds a new book
def add_book(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'])
    return redirect('/books')
#show book review page for selected book
def show_review(request, id):
    book = Book.objects.get(id=id)
    context = {
    'title': book.title,
    'author': book.author
    }
    return render(request, 'books/show_review.html', context)
#left off here, need to get this to work
def add_review(request, id):
    book = Book.objects.get(id=id)
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'])
    return redirect('/books')

#destroy a book! Have to enable in books/index.html for this to work, it is commented out
def destroy(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')
