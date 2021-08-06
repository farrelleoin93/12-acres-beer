from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from beers.models import Beer


def bag_contents(request):

    bag_items = []
    beer_total = 0
    combined_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    print(bag)

    for item_id, quantity in bag.items():
        beer_product = get_object_or_404(Beer, pk=item_id)
        beer_total += quantity * beer_product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'beer_product': beer_product,
        })

    if combined_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = combined_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - combined_total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + combined_total

    context = {
        'bag_items': bag_items,
        'beer_total': beer_total,
        'combined_total': combined_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
