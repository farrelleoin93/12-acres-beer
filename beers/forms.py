from django import forms
from .widgets import CustomClearableFileInput
from .models import Beer, Category, BeerReview


class BeerForm(forms.ModelForm):

    class Meta:
        model = Beer
        fields = '__all__'
        exclude = ('average_rating',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ReviewForm(forms.ModelForm):

    class Meta:
        model = BeerReview
        exclude = ('beer', 'user', 'date_added', 'verified_purchase')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'review-form-input'
        self.fields['body'].widget.attrs = {'rows': 4}
