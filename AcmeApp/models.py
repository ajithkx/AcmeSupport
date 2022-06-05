from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager  
from django.utils import timezone  
from django.utils.translation import gettext as _
from account.models import CustomUserManager
# Create your models here.



class CustomUser(AbstractUser):
	first_name = None
	last_name = None
	date_joined = None
	username = models.CharField(max_length=50, null=False)
	phone = models.CharField(max_length=10, null=True)
	email = models.EmailField(_('email address'), unique=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	last_updated_at = models.DateTimeField(auto_now_add=True, null=True)
	created_by = models.CharField(max_length=50, null=True)
	
	ROLE_CHOICES = (
		('admin','Admin'),
		('user', 'User')
	)
	role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')

	# department = models.ForeignKey("Department", on_delete=models.CASCADE)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	objects = CustomUserManager()

    
	def __str__(self):
	    return self.username

class Department(models.Model):
    name = models.CharField(max_length=50, null=True)