from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# home
class HomeView(TemplateView):
    template_name = 'home\index.html'
    

# about us
class AboutView(TemplateView):
    template_name = 'home\website_about.html'