# recommendations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_recommendations, name='movie_recommendations'),  # This maps the root of /recommendations/ to the movie_recommendations view
]

