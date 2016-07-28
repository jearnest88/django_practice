from django.shortcuts import render, redirect
from .models import Product

#main page
def index(request):
	#pull products from DB
	products=Product.objects.all()
	context={
		'products' : products
	}
	#show products on index page
	return render(request, 'product/index.html', context)

#directs to creat page
def new(request):
	return render(request, 'product/create.html')

#creates products
def create(request):
    #pulls from form.....
	if request.method == 'POST':
		name=request.POST.get('name')
		description=request.POST.get('description')
		price=request.POST.get('price')

		#and pushes to DB
		Product.objects.create(name=name,description=description,price=price)

	return redirect('/')

#show page, displays single item
def show(request, id):
	#pulls the selected product by grabbing the ID
	product=Product.objects.get(id=id)
	context={
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	return render(request, 'product/show.html', context)

#the edit page, to change something about a product
def edit(request, id):
    #pulls the selected product by grabbing the ID
	product=Product.objects.get(id=id)
	context={
		'id' : id,
		'name' : product.name,
		'description' : product.description,
		'price' : product.price
	}
	return render(request, 'product/edit.html', context)

#this is the actual method that changes the product. Edit puts everything in place
# and change commits the change
def change(request, id):
	#pulls the selected product by grabbing the ID
	product=Product.objects.get(id=id)
	#grabs form information
	product.name=request.POST.get('name')
	product.description=request.POST.get('description')
	product.price=request.POST.get('price')
	product.save()

	return redirect('/')

#this deletes items from the page and DB
def delete(request, id):
	#pulls the selected product by grabbing the ID
	product=Product.objects.get(id=id)
	product.delete()
    
	return redirect('/')
