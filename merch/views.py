from django.shortcuts import render, get_object_or_404
from .models import Merch


def merch(request):
    """ A view to show merchandise """

    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merch/merch.html', context)


def merch_detail(request, merch_id):
    """ A view to show merchandise products details """

    merch = get_object_or_404(Merch, pk=merch_id)

    context = {
        'merch': merch,
    }

    return render(request, 'merch/merch_detail.html', context)

