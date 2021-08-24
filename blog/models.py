from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title
