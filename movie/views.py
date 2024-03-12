from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .forms import MovieCreateForm
from django.urls import reverse_lazy
from .models import Movie

# Create your views here.

# movie list view
class MovieListView(ListView):
    model = Movie
    template_name = 'movie\movie_list.html'
    context_object_name = 'movies'
    
    
    
# movie detail view
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie\movie_detail.html'
    context_object_name = 'detail'
    

# movie update view
class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'movie\movie_update.html'
    fields = ['name']
    
    
    
# movie delete view
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movie\movie_delete.html'
    success_url = reverse_lazy('home')
    
    
# movie create view
@login_required
def create_movie(request):
    if request.method == 'POST':
        
        form = MovieCreateForm(request.POST , request.FILES)
        
        if form.is_valid() :
            cd = form.cleaned_data
            Movie.objects.create(
                user = request.user,
                name = cd['name'],
                genre = cd['genre'],
                time = cd['time'],
                summary = cd['summary'],
                age = cd['age'],
                photo = cd['photo'],
                slug = cd['slug']
            )
            messages.success(request, 'your movie was created successfuly!', 'success')
            
            
        else:
            messages.error(request, 'please fill out the fields correctly!', 'danger')
            return render (request , 'movie\movie_create.html' , {'form':form}) 
    return render (request, 'movie\movie_create.html', {'form':MovieCreateForm} )