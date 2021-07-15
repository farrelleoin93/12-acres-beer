from django.shortcuts import render
from .models import Beer


def beers(request):
    """ A view to show beers """

    beers = Beer.objects.all()

    context = {
        'beers': beers,
    }

    return render(request, 'beers/beers.html', context)
