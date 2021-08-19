from django.shortcuts import render, HttpResponse
from shop.models import Product

def home(request):
	products = Product.objects.all().order_by('point')

	context = {
		'products': products,
	}
	return render(request, 'base/home.html', context)
