from django import forms
from .models import Newsletter


class ContactForm(forms.Form):
    """
    Contact Form for contact page
    """
    name = forms.CharField(required=True, label='Name')
    from_email = forms.EmailField(required=True, label='Email')
    email_subject = forms.CharField(required=True, label='Subject')
    email_message = forms.CharField(
        widget=forms.Textarea,
        required=True, label='Message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True


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
