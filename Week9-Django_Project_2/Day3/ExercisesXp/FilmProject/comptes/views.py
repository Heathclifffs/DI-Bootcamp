from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Create your views here.

#.................................................................
#class logout

def logout_user(request):
    
    logout(request)
    return redirect('homepage')
#.........................................................................    
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('homepage')
        message = 'Identifiants invalides.'
    return render(request, 'connexion/login.html', context={'form': form, 'message': message})
#.........................................................................    

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'connexion/register.html', context={'form': form})    
#..............................................
def profile(request,id):
    User = get_user_model()
    profile=User.objects.filter(id=id)
    context={
        'profile':profile
    }
    return render(request,'connexion/profile.html',context)
#........................................................
