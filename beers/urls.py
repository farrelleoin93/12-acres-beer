from django.urls import path
from . import views

urlpatterns = [
    path('', views.beers, name='beers'),
    path('<int:beer_id>/', views.beer_detail, name='beer_detail'),
    path('add/', views.add_beer, name='add_beer'),
    path('edit/<int:beer_id>/', views.edit_beer, name='edit_beer'),
    path('delete/<int:beer_id>/', views.delete_beer, name='delete_beer'),
    path('add_review/<int:beer_id>/', views.add_review, name='add_review'),
    path(
        'edit_review/<int:review_id>/',
        views.edit_review, name='edit_review'),
    path(
        'delete_review/<int:review_id>/',
        views.delete_review, name='delete_review'),
]
