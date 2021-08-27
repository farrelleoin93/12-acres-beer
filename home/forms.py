from django import forms
from .models import Newsletter


class ContactForm(forms.Form):
    """
    Contact Form for contact page
    """
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    email_subject = forms.CharField(required=True)
    email_message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'from_email': 'Your Email',
            'email_subject': 'Subject',
            'email_message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email_address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email_address': 'Email Address',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
