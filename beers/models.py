from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Beer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    average_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                         null=True, blank=True)
    image_url = models.URLField(max_length=324, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def calculate_rating(self):
        """
        Calculate the beers average rating
        """
        self.average_rating = self.reviews.all().aggregate(Avg("rating"))[
            'rating__avg']
        self.save()

    def __str__(self):
        return self.name


class BeerReview(models.Model):
    """
    A model to review beers.
    """
    class Meta:
        ordering = ['-date_added']

    RATING_OPTIONS = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    beer = models.ForeignKey(Beer,
                                null=True,
                                blank=True,
                                related_name='reviews',
                                on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    body = models.TextField()
    rating = models.IntegerField(choices=RATING_OPTIONS, default=3)
    date_added = models.DateTimeField(auto_now_add=True)
    verified_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.title
