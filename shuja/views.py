from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        if full_name == "":
            messages.warning(request, 'Please Enter your Name')
        elif email == "":
            messages.warning(request, 'Please Enter your Email')
        elif message == "":
            messages.warning(request, 'Please Enter your Message')
        else:
            # Contact.objects.create(name=full_name, email=email, message=message)
            # send_mail(full_name, message, settings.EMAIL_HOST_USER, [email])
            messages.success(request, 'Thanks for reaching me, I have received your Message.')
    return render(request, 'shuja/index.html')
