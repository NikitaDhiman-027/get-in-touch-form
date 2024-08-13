from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')

    return render(request, 'index.html')
