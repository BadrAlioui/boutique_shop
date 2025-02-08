from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import NewsletterForm
from .models import NewsletterSubscriber

def subscribe_newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                form.save()
                
                # Envoi de l'email
                send_mail(
                    'Welcome to our Newsletter!',
                    'Thank you for subscribing to our newsletter. Stay tuned for updates!',
                    'studentinstitute2024@gmail.com',
                    [email],
                    fail_silently=False,
                )
                
                messages.success(request, "You have successfully subscribed to our newsletter!")
            else:
                messages.warning(request, "You are already subscribed.")
        else:
            messages.error(request, "Invalid email address.")
    return redirect('home')
