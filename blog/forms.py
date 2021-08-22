from django import forms
from .widgets import CustomClearableFileInput
from .models import Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False,
        widget=CustomClearableFileInput
    )
