from django.contrib import messages

from .forms import NewsletterForm
from .models import Newsletter


def newsletter(request):
    """
    A view to allow the user to subscribe to the newsletter
    """
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            instance = newsletter_form.save(commit=False)
            if Newsletter.objects.filter(
                    email_address=instance.email_address).exists():
                messages.error(request,
                               'Sorry, the email already exists in our list')
            else:
                newsletter_form.save()
                newsletter_form = NewsletterForm()
                messages.success(request,
                                 'Thank you very much for subscribing \
                                 to our newsletter')
    else:
        newsletter_form = NewsletterForm()

    context = {
        'newsletter_form': newsletter_form,
        }

    return context
