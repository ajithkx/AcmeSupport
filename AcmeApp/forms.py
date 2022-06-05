from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'email','role', 'password1', 'password2']