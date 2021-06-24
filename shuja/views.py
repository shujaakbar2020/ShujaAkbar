from django.shortcuts import render
from .models import Contact
from django.contrib import messages


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
            Contact.objects.create(name=full_name, email=email, message=message)
            messages.success(request, 'Thanks for reaching me, I have received your Message.')

    return render(request, 'shuja/index.html')
