from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import views
# Create your views here.




def home(request):
    return render(request, 'logg/home.html')

def about(request):
    return render(request, 'logg/about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for account {username}')
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'logg/register.html', {'form':form})


def login(request):
    #return render(request, 'logg/login.html')
    return redirect('about')


def logout(request):
    return render(request, 'logg/logout.html')

@login_required
def profile(request):
    return render(request, 'logg/profile.html')