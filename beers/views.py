from django.shortcuts import render, get_object_or_404
from .models import Beer


def beers(request):
    """ A view to show beers """

    beers = Beer.objects.all()

    context = {
        'beers': beers,
    }

    return render(request, 'beers/beers.html', context)


def beer_detail(request, beer_id):
    """ A view to show beer details """

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'beers/beer_detail.html', context)

