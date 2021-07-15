from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)


class Beer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=324, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name