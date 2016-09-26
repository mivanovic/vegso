from django.shortcuts import render


def index(request):
	return render(request, 'landing.html')


def references(request):
	return render(request, 'landing.html')


def blog(request):
	return render(request, 'landing.html')