from django.contrib import admin
from .models import Beer, Category


class BeerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'abv',
        'category',
        'price',
        'image_url',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
