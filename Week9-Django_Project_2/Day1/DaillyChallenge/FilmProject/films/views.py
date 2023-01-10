from django.shortcuts import render
from .forms import AddFilmForm,AddDirectorForm
from . import forms
from django.contrib import messages
from .models import Categorie,Pays,Directeur,Film

# Create your views here.
def home(request):
    film=Film.objects.all()
    context={
        'film':film
    }
    return render(request,'homepage.html',context)
#........................................
def add_film(request):
    form= forms.AddFilmForm()
    if request.method== 'POST':
        form=forms.AddFilmForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=AddFilmForm()
    return render(request,'film/AddFilm.html',{'form':form})
#.................................
#Director form
def add_director(request):
    form= forms.AddDirectorForm()
    if request.method== 'POST':
        form=forms.AddDirectorForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=AddDirectorForm()
    return render(request,'directeur/AddDirector.html',{'form':form})