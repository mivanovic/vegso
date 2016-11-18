from django.shortcuts import render


def index(request):
	return render(request, 'landing.html')


def references(request):
	return render(request, 'references.html')


def ref_item(request, id):
	return render(request, 'ref_item.html')


def blog(request):
	return render(request, 'landing.html')