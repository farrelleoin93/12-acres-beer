from django.urls import path
from . import views

urlpatterns = [
    path('findbeers', views.findbeers, name='findbeers'),
]
