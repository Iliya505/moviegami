from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView
from .models import Movie

# Create your views here.

class MovieListView(ListView):
    model = Movie
    template_name = 'movie\movie_list.html'
    context_object_name = 'movies'
    
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie\movie_detail.html'
    context_object_name = 'detail'
    
# class MovieCreateView(CreateView):
#     model = Movie
#     template_name = 'movie/movie_create.html'
#     fields = ['name' , 'genre' , 'time' , 'summary' , 'age' , 'photo' , 'slug']
    
class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie\movie_update.html'
    fields = ['name']