from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
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
    

    
class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'movie\movie_update.html'
    fields = ['name']
    
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie\movie_delete.html'
    success_url = reverse_lazy('home')