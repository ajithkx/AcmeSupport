from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        role = None
        if request.user.role is not None:
            role = request.user.role

        if role == 'admin' or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page')
    return wrapper_func