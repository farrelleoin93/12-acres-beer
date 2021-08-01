from django.shortcuts import render
from django.conf import settings

# Create your views here.


def findbeers(request):
    """ A view to return the findbeers page """

    context = {
        'maps_api_key': settings.MAPS_API_KEY,
    }

    return render(request, "findbeers/findbeers.html", context)
