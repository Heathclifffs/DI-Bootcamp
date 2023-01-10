from django import forms
from .models import Pays,Categorie,Directeur,Film
from . import models
#...............................
class FilmForm(forms.ModelForm):
    class Meta:
        model=models.Film
        fields=['titre','date_sortie','film_nationalite','pays_disponible','categorie','realisateurs','afficher']
#....................................
class DirectorForm(forms.ModelForm):
    edit_directeur = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model=models.Directeur
        fields=['prenom','nom']
#.................................
class PaysForm(forms.ModelForm):
    class Meta:
        model=models.Pays
        fields=['nom']
#..............................
class PosteForm(forms.ModelForm):
    class Meta:
        model=models.Poste
        fields=['image']