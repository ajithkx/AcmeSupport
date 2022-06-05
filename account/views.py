import email
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.template import context
from AcmeApp.views import home
from .decorators import unauthenticated_user
# Create your views here.
@unauthenticated_user
def Login(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password =request.POST.get('password')

			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Email OR password is incorrect')

		context = {}
		return render(request, 'account/login.html', context)

def Logout(request):
	logout(request)
	return redirect('login')
    