from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Beer


def beers(request):
    """ A view to show beers """

    beers = Beer.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('beers'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            beers = beers.filter(queries)

    context = {
        'beers': beers,
        'search_term': query,
    }

    return render(request, 'beers/beers.html', context)


def beer_detail(request, beer_id):
    """ A view to show beer details """

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'beers/beer_detail.html', context)
