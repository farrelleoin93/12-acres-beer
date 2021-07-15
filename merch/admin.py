from django.contrib import admin
from .models import Merch


class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'sku',
        'has_sizes',
        'category',
        'price',
        'image_url',
        'image',
    )


admin.site.register(Merch, MerchAdmin)
