from django import forms
from .models import Pays,Categorie,Directeur,Film
from . import models
#...............................
class AddFilmForm(forms.ModelForm):
    class Meta:
        model=models.Film
        fields=['titre','date_sortie','film_nationalite','pays_disponible','categorie']
#....................................
class AddDirectorForm(forms.ModelForm):
    class Meta:
        model=models.Directeur
        fields=['prenom','nom']