from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST.get":
		message_name = request.POST.get['message-name']
		message_email = request.POST.get['message-email']
		message = request.POST.get['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['univdentalclinic@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST.get":
		your_name = request.POST.get['your-name']
		your_phone = request.POST.get['your-phone']
		your_email = request.POST.get['your-email']
		your_address = request.POST.get['your-address']
		your_schedule = request.POST.get['your-schedule']
		your_date = request.POST.get['your-date']
		your_message = request.POST.get['your-message']
		
		# send an email
		appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			['univdentalclinic@gmail.com'], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
			})

	else:
		return render(request, 'home.html', {})
