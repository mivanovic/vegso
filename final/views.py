from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def index(request):
	return render(request, 'landing.html')


def references(request):
	return render(request, 'references.html')


def ref_item(request, id):
	return render(request, 'ref_item.html')


def blog(request):
	return render(request, 'landing.html')


def send_email(request):
	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		send_mail(
			'www.final-st.hr',  # subject
			message + '\n\n Ime: {} \n Tel: {} \n Email: {}'.format(name, phone, email),
			email,  # from
			[settings.EMAIL_HOST_USER],  # to
			fail_silently=False,
		)

		return HttpResponse('')