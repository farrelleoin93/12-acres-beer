from django.urls import path
from . import views

urlpatterns = [
    path('', views.beers, name='beers'),
    path('<beer_id>', views.beer_detail, name='beer_detail'),
]
