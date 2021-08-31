from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BeerReview


@receiver(post_save, sender=BeerReview)
def update_rating_on_save(sender, instance, created, **kwargs):
    """
    Update a beers average rating when a review
    is created or updated.
    """
    if instance.beer:
        instance.beer.calculate_rating()


@receiver(post_delete, sender=BeerReview)
def update_rating_on_delete(sender, instance, **kwargs):
    """
    Update a beers average rating when a review is deleted.
    """
    if instance.beer:
        instance.beer.calculate_rating()
