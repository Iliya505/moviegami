from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


# django register
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    
# enc register
def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(
                username = cd['username'],
                password = cd['password'],
                email = cd['email']
            )
            messages.success(request, 'your user was created successfuly!', 'success')
        
        else:
            messages.error(request, 'please fill out the fields correctly!', 'danger')
            return render (request , 'registration\encregister.html' ,{'form':form})
    return render (request , 'registration\encregister.html' , {'form':UserRegisterForm})