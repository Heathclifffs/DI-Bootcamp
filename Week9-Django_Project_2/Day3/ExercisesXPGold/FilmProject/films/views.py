from django.shortcuts import render
from .forms import FilmForm,DirectorForm,PosteForm,DeleteFilmForm,CommentaireForm
from . import forms
from django.contrib import messages
from films.models import Categorie,Pays,Directeur,Film,Poste,Commentaire
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from . import models
from django.contrib import messages


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
            messages.success(request, 'Film ajoutez avec succes') # ignored
            return redirect('homepage')
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
#..................................................
def add_poste(request):
    form_f= forms.FilmForm()
    form= forms.PosteForm()
    if request.method== 'POST':
        form_f=forms.FilmForm(request.POST)

        form=forms.PosteForm(request.POST)
        if form.is_valid() and form_f.is_valid():
            form= form.save(commit=False)
            form_f= form.save(commit=False)
            form.save()
            form_f.save()
            form_f=FilmForm()
            form=PosteForm()
            return redirect('homepage')

    return render(request,'poste/AddPoste.html',{'form':form,'form_f':form_f})
#................................................................
def suprimer(request,id):
    film =get_object_or_404(models.Film, id=id)
    form= forms.FilmForm(instance=film)
    # s=Services.objects.filter(models.Services,author_id=service_id)
    delete_form = forms.DeleteFilmForm()
    if request.method == 'POST':    
            form= forms.FilmForm(instance=film)
            if 'delete_film' in request.POST:
                delete_form = forms.DeleteFilmForm(request.POST)
                if delete_form.is_valid():
                    film.delete()
                    messages.success(request, 'Film suprimer avec success') # ignored
                    return redirect('homepage')
    context = {
        'delete_form': delete_form,
        'form':form,
        'messages':messages
        }
    return render(request, 'film/delete_film.html',context)
#.......................................................................
def add_commentaire(request,id):
    form_c= forms.CommentaireForm()
    film=Film.objects.filter(id=id)
    if request.method== 'POST':
        form_c=forms.CommentaireForm(request.POST)

        form=forms.CommentaireForm(request.POST)
        if form_c.is_valid():
            form_c= form.save(commit=False)
            form_c=request.user
            form.save()
            form_c.save()
            form_c=CommentaireForm()
            return redirect('homepage')

    return render(request,'commentaire/commentaire.html',{'form_c':form_c,'film':film})
#............................................................
def voir_commentaire(request,id):
    commentaire=Commentaire.objects.filter(id=id)
    film=Film.objects.filter(id=id)
   

    return render(request,'commentaire/voir_commentaire.html',{'commentaire':commentaire,'film':film})