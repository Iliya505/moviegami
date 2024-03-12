from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<str:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie_edit/<str:slug>/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movie_delete/<str:slug>/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movie_create/', views.create_movie, name='movie_create')
]
