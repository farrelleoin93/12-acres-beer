from django.contrib import admin
from .models import Post


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'content',
        'image',
        'date_added',
        'author',
    )

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, BlogPostAdmin)
