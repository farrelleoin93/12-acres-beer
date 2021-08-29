from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            "default_phone_number": "Phone number",
            "default_email": "Phone number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or city",
            "default_county": "County",
            "default_country": "Country",
            "default_postcode": "Postcode",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
