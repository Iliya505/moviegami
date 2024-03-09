from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Movie

# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = 'movie\movie_list.html'
    context_object_name = 'movies'