from django import forms 
from .models import Movie


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user','created','updated','published',)