from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email_address',
        'date_subscribed',
    )


admin.site.register(Newsletter, NewsletterAdmin)
