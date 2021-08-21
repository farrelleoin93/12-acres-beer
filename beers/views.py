from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Beer, Category
from .forms import BeerForm


def beers(request):
    """ A view to show beers """

    beers = Beer.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            beers = beers.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('beers'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            beers = beers.filter(queries)

    context = {
        'beers': beers,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'beers/beers.html', context)


def beer_detail(request, beer_id):
    """ A view to show beer details """

    beer = get_object_or_404(Beer, pk=beer_id)

    context = {
        'beer': beer,
    }

    return render(request, 'beers/beer_detail.html', context)


def add_beer(request):
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added beer!')
            return redirect(reverse('add_beer'))
        else:
            messages.error(request, 'Failed to add beer. Please ensure the form is valid.')
    else:
        form = BeerForm()

    template = 'beers/add_beer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
