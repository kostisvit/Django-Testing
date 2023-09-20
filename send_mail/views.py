# views.py import what you have not imported before

import email
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm
from django.http import HttpResponse

def compose_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            bcc = [email.strip() for email in form.cleaned_data['bcc'].split(',') if email.strip()]
            
            # Create an EmailMessage object to handle attachments
            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL,[email], bcc=bcc)
            
            # Attach files to the email
            for attachment in request.FILES.getlist('attachments'):
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            
            try:
            
            # Send the email
                email.send()
            # Handle success or error here
                return render(request, 'email_sent.html')
            except Exception as e:
                return HttpResponse(f'Email could not be sent. Error: {str(e)}')
            
    else:
        if request.user.is_authenticated:
            user_email = request.user.email
            form = EmailForm(initial={'email': user_email})
        else:
            form = EmailForm()
    
    return render(request, 'email.html', {'form': form})