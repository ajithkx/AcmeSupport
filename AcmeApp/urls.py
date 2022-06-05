from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),  
	path('createUser/', views.UserCreation, name="user_creation"),  
	path('manageTicket/', views.manageTicket, name="manageTicket"),  
	path('createTicket/', views.createTicket, name="createTicket"),  
]