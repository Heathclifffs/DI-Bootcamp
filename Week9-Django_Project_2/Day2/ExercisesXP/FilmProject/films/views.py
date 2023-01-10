from django.shortcuts import render
from .forms import FilmForm,DirectorForm
from . import forms
from django.contrib import messages
from films.models import Categorie,Pays,Directeur,Film
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from . import models

# Create your views here.
def home(request):
    film=Film.objects.all()
    context={
        'film':film
    }
    return render(request,'homepage.html',context)
#........................................
def add_film(request):
    form= forms.FilmForm()
    if request.method== 'POST':
        form=forms.FilmForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=FilmForm()
    return render(request,'film/AddFilm.html',{'form':form})
#.................................
#Director form
def add_director(request):
    form= forms.DirectorForm()
    if request.method== 'POST':
        form=forms.DirectorForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.save()
            form=DirectorForm()
    return render(request,'directeur/AddDirector.html',{'form':form})
#.............................................................
#fonction modifier directeur 
def edit_directeur(request,id):
    directeur=get_object_or_404(models.Directeur,id=id)
    edit_form= forms.DirectorForm(instance=directeur)
    if request.method=='POST':
        if 'edit_directeur' in request.POST:
            
            edit_form= forms.DirectorForm(request.POST, instance=directeur)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('homepage')
    context={
        'edit_form':edit_form
    }
    return render(request,'directeur/edit_directeur.html',context)
#.................................................................
#fonction modifier un film
def edit_film(request,id):
    film=get_object_or_404(models.Film,id=id)
    edit_form= forms.FilmForm(instance=film)
    if request.method=='POST':
        if 'edit_film' in request.POST:
            
            edit_form= forms.FilmForm(request.POST, instance=film)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('homepage')
    context={
        'edit_form':edit_form
    }
    return render(request,'film/edit_film.html',context)