from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('encregister/', views.register_page, name='encregister'),
]
