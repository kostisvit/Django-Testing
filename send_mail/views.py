# views.py import what you have not imported before

import email
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm



def send_email_with_attachment(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            

            # Create an EmailMessage object
            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

            # Attach the file if provided
            if 'attachments' in request.FILES:
                attachments = request.FILES['attachments']
                email.attach(attachments.name, attachments.read(), attachments.content_type)

            # Send the email
            email.send()

            return render(request, 'email_sent.html')
    else:
        form = EmailForm()

    return render(request, 'email.html', {'form': form})