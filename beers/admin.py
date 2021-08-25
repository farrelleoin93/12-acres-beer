from django.contrib import admin
from .models import Beer, Category, BeerReview


class BeerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'abv',
        'category',
        'price',
        'average_rating',
        'image_url',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BeerReviewAdmin(admin.ModelAdmin):
    list_display = (
        'beer',
        'user',
        'date_added',
        'rating',
    )
    ordering = ('date_added',)


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BeerReview, BeerReviewAdmin)
