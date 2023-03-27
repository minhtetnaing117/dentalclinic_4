from django.shortcuts import render

def index(request):
	return render(request,'home.html', {})

def error(request):
	return render(request,'404.html', {})

def about(request):
	return render(request,'about.html', {})