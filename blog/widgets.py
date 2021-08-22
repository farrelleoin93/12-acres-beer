from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Blog Image')
    input_text = _('')
    template_name = (
        'blog/custom_widget_template/'
        'custom_clearable_file_input.html'
    )
