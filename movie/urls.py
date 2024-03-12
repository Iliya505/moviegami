from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<str:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    # path('movie_create/', views.MovieCreateView.as_view(), name='movie_create')
    path('movie_edit/<str:slug>/', views.MovieUpdateView.as_view(), name='movie_edit'),
]
