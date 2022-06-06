from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from .forms import CreateUserForm
import requests
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
	
	url = "https://acmesupportsupport.zendesk.com/api/v2/tickets"

	payload={}
	headers = {
	'Authorization': 'Basic YWppdGhreEBnbWFpbC5jb20vdG9rZW46aGMwOG8zbWhLclFNUTB5SHZFMWQ0MG5MdWFPb3lyYXBac084a2l6cQ==',
	'Cookie': '__cfruid=73c088da2a2af97d44603cb79132fdfa1b96b3ab-1654512615; _zendesk_cookie=BAhJIhl7ImRldmljZV90b2tlbnMiOnt9fQY6BkVU--459ed01949a36415c1716b5711271c3d08918307'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	print(response.text)
	context={}
	context["res"]=response.text
	return render(request,'AcmeApp/createTicket.html',context)
