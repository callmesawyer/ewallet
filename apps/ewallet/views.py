from django.shortcuts import render
from django.http import HttpResponse

# function based views

# def home(request):
# 	return HttpResponse('Hello World! This is a homepage.')

def home(request):
	context = {
		'title': 'Home Page',
		'name' : 'Roshan'
	}
	return render(request, 'home.html', context)

def contact(request):
	return HttpResponse('Contact Page!')

