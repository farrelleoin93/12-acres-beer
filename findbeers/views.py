from django.shortcuts import render

# Create your views here.


def findbeers(request):
    """ A view to return the findbeers page """

    return render(request, "findbeers/findbeers.html")
