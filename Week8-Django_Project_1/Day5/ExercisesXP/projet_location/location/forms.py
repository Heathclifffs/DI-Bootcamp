from django import forms
from . import models
from .models import Client,Vehicule,Location,TailleVehicule,TarifLocation,TypeVehicule
#...................
class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Client
        fields=['prenom']
#.........................................................................
class VehiculeForm(forms.Form):
    type=forms.CharField(max_length=20)
#........................................................................
class ClientAddForm(forms.ModelForm):
    class Meta:
        model=models.Client
        fields=['prenom','nom','email','numero','adresse','ville','pays']
#......................................................................
class VehiculeAddForm(forms.Form):
    nom=forms.CharField(max_length=30)
    prix=forms.DecimalField(max_digits=6,decimal_places=2)
    taille=forms.CharField(max_length=30)
    