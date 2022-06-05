from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from .forms import CreateUserForm
from account.decorators import admin_only
# Create your views here.

@login_required(login_url='login')
def home(request):
	context = {}
	return render(request, 'AcmeApp/home.html', context)

@login_required(login_url='login')
@admin_only
def UserCreation(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.created_by = request.user.username
			post.last_updated_at = timezone.now()
			post.created_at = timezone.now()
			post.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('user_creation')
		

	context = {'form':form}
	return render(request, 'AcmeApp/user_creation.html', context)

@login_required(login_url='login')
def manageTicket(request):
	context=[]
	return render(request,'AcmeApp/manageTicket.html')


@login_required(login_url='login')
def createTicket(request):
	context=[]
	return render(request,'AcmeApp/createTicket.html')