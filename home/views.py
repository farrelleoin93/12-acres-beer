from django.shortcuts import render, redirect
from .forms import ContactForm

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")


def contact(request):
    """
    A view to return the contact page
    """
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            email_subject = form.cleaned_data['email_subject']
            email_message = form.cleaned_data['email_message']
            try:
                send_mail(email_subject, email_message, from_email,
                          [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            messages.success(request, (
                'Thank you for contacting 12 Acres, '
                'A member of our staff will contact you as soon as possible.'))
            return redirect('home')

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
