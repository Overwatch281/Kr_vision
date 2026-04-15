from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message

def contact(request):
    if request.method == 'POST':
        Message.objects.create(
            name    = request.POST.get('name'),
            email   = request.POST.get('email'),
            subject = request.POST.get('subject'),
            body    = request.POST.get('body'),
        )
        messages.success(request, 'Votre message a bien été envoyé !')
        return redirect('contact')
    return render(request, 'contact/contact.html')

from .models import Message, Newsletter

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.get_or_create(email=email)
            messages.success(request, 'Vous êtes bien inscrit à notre newsletter !')
    return redirect(request.META.get('HTTP_REFERER', '/'))