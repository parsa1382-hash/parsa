from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Product, Sell

def shop(request, category_id):
	products = Product.objects.filter(category=category_id)

	context = {
		'products': products,
	}
	return render(request, 'shop/shop.html', context)

def product(request, product_id):
	product = get_object_or_404(Product, pk=product_id)

	context = {
		'product': product,
	}
	return render(request, 'shop/product.html', context)

def buy(request, product_id):
	product = get_object_or_404(Product, pk=product_id)

	context = {
		'product': product,
	}
	return render(request, 'shop/buy.html', context)

def instagram(request, product_id):
	product = get_object_or_404(Product, pk=product_id)

	context = {
		'product': product,
	}
	return render(request, 'shop/instagram.html', context)

def save_sell(request, product_id):
	if request.method == 'POST':

		name = request.POST['name']
		product = get_object_or_404(Product, pk=product_id)
		phone = request.POST['phone']
		address = request.POST['address']

		sell = Sell(product=product, phone=phone, address=address, name=name)
		sell.save()

		return redirect('base:home')
	else:
		return redirect('base:home')
