from django.shortcuts import render, redirect
from .forms import ProductForm, SalesForm
from .models import Product


# Create your views here.

reorders = []
processed_reorders = []

def add_product(request):
	form = ProductForm

	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('list_products')

	else:
		form = ProductForm		
	return render(request, "add_product.html", {"form":form})


def list_products(request):
	products = Product.objects.all()
	return render(request, "all_products.html", {"products":products})


def sell_product(request,pk):
	form = SalesForm
	product = Product.objects.get(pk=pk)
		
	if request.method == 'POST':
		form = SalesForm(request.POST)
		if form.is_valid():
			product.quantity -= form.cleaned_data['quantity_sold']
			product.save()

			return redirect('list_products')

	else:
		form = SalesForm			
					
	return render(request, "sell_product.html", {"form":form})


def unprocessed_reorders(request):
	products = Product.objects.all()

	for product in products:
		if product.quantity <= product.reorder_level:
			reorders.append(product)
			product.save()
	return render(request, "unprocessed_reorders.html", {"reorders":reorders}, {"products":products})	



def dispatch_reorder(request):
	products = Product.objects.all()

	for product in products:
		for reorder in reorders:
			if product.name == reorder.name:
				product.quantity += product.default_quantity
				processed_reorders.append(product)
				product.save()
				reorders.remove(product)
				# return redirect("list_products")

	return render(request, "processed_reorders.html", {"processed_reorders":processed_reorders}, {"products":products})	

