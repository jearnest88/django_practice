from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	context = {
		'products': Product.objects.all()
	}
	return render(request, 'product/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        Product.objects.create(name=name, description=description, price=price)


    return render(request, 'product/create.html')
# Create your views here.
