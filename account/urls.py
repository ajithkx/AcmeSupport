from django.urls import path
from . import views
import AcmeApp 
urlpatterns = [
	path('login/', views.Login, name="login"),  
	path('logout/', views.Logout, name="logout"),
	path('', AcmeApp.views.home, name="home"),  

]