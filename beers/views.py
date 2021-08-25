from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .models import Beer, Category, BeerReview
from profiles.models import UserProfile
from checkout.models import OrderLineItem

from .forms import BeerForm, ReviewForm


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
    form = ReviewForm()

    context = {
        'beer': beer,
        'form': form,
    }

    return render(request, 'beers/beer_detail.html', context)


@login_required
def add_beer(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES)
        if form.is_valid():
            beer = form.save()
            messages.success(request, 'Successfully added beer!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request, 'Failed to add beer. Please ensure the form is valid.')
    else:
        form = BeerForm()

    template = 'beers/add_beer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_beer(request, beer_id):
    """ Edit a beer in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    beer = get_object_or_404(Beer, pk=beer_id)
    if request.method == 'POST':
        form = BeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated beer!')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(request, 'Failed to update beer. Please ensure the form is valid.')
    else:
        form = BeerForm(instance=beer)
        messages.info(request, f'You are editing {beer.name}')

    template = 'beers/edit_beer.html'
    context = {
        'form': form,
        'beer': beer,
    }

    return render(request, template, context)


@login_required
def delete_beer(request, beer_id):
    """ Delete a beer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only 12 Acres owners can do that.')
        return redirect(reverse('home'))

    beer = get_object_or_404(Beer, pk=beer_id)
    beer.delete()
    messages.success(request, 'Beer deleted!')
    return redirect(reverse('beers'))


def add_review(request, beer_id):
    """ Add a review for a beer """
    beer = get_object_or_404(Beer, pk=beer_id)
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user_id=request.user)
    else:
        profile = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            reviews = beer.reviews.all()

            if reviews.filter(user=request.user).exists():
                messages.info(
                    request, f"You've already reviewed {beer.name}")
                return redirect(reverse('beer_detail', args=[beer.id]))

            if form.is_valid():
                review = form.save(commit=False)
                review.beer = beer
                review.user = request.user
                # Check if user has purchased the beer
                if OrderLineItem.objects.filter(
                    order__user_profile=profile).filter(
                        beer=beer).exists():
                    review.verified_purchase = True

                review.save()
                messages.info(
                    request,
                    'Thanks for the review')

                return redirect(reverse('beer_detail', args=[beer.id]))
            else:
                messages.error(
                    request,
                    "Failed to add review - please try again")

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, context)


def edit_review(request, review_id):
    """
    Edit a review
    """
    review = get_object_or_404(BeerReview, pk=review_id)
    beer = review.beer

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'You updated a review')
            return redirect(reverse('beer_detail', args=[beer.id]))
        else:
            messages.error(
                request,
                "Failed to update review - please try again")

    else:
        form = ReviewForm(instance=review)

    messages.info(request, f"You are editing your review of {beer}.")
    template = 'beers/beer_detail.html'
    context = {
        'form': form,
        'review': review,
        'beer': beer,
        'edit': True,
    }

    return render(request, template, context)
