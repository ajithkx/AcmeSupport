from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import context
from .forms import CreateUserForm
import requests,json
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
	
        # Package the data for the API
	data = {'request': {'subject': "Test", 'comment': {'body': "THIS IS A TEST"}}}
	payload={
		"ticket": {
			"comment": {
			"body": "The smoke is very colorful."
			},
			"priority": "urgent",
			"subject": "My printer is on fire!"
		}
	}
	ticket = json.dumps(payload)
	# Make the API request
	user = "ajithkx@gmail.com" + '/token'
	api_token = 'hc08o3mhKrQMQ0yHvE1d40nLuaOoyrapZsO8kizq'
	url = 'https://acmesupportsupport.zendesk.com/api/v2/tickets.json'
	headers = {'content-type': 'application/json'}
	r = requests.post(
		url,
		data=ticket,
		auth=(user, api_token),
		headers=headers
	)

	# url = "https://acmesupportsupport.zendesk.com/api/v2/tickets/"

	
	# headers = {
	# 'Authorization': 'Basic YWppdGhreEBnbWFpbC5jb20vdG9rZW46aGMwOG8zbWhLclFNUTB5SHZFMWQ0MG5MdWFPb3lyYXBac084a2l6cQ==',
	# }

	# response = requests.request("POST", url, headers=headers, data=payload)

	context={}
	context["res"]=r.text
	return render(request,'AcmeApp/createTicket.html',context)
