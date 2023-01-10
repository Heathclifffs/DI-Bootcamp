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
    nom=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'placeholder':'nom du directeur'
            
        }
    ))
    prenom=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'placeholder':'prenom du directeur'
        }
    ))
    class Meta:
        model=models.Directeur
        fields=['nom','prenom']
#.................................
class PaysForm(forms.ModelForm):
    nom=forms.CharField(label='',required=True,widget=forms.TextInput(
        attrs={
            'placeholder':'nom du pays'
        }
    ))
    class Meta:
        model=models.Pays
        fields=['nom']