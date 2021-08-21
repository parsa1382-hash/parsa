from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from shop.models import Sell, Buy

def login_view(request):
	return render(request, 'user/login.html')

def register_view(request):
	return render(request, 'user/register.html')

def register(request):
	user = request.POST['username']

	return render(request, 'user/profile.html')

def profile(request):
	if request.user.is_authenticated:
		sells = Sell.objects.all()
		buys = Buy.objects.filter(user=request.user)

		context = {
			'sells': sells,
			'buys': buys,
		}
		return render(request, 'user/profile.html', context)
	else:
		return redirect('user:login_view')

def check(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('user:profile')
		else:
			messages.add_message(request, messages.INFO, 'Bad Username/Password')
			return redirect('user:login_view')