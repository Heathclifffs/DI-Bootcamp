from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Client(models.Model):
    prenom=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    email=models.EmailField()   
    numero = PhoneNumberField()
    adresse=models.CharField(max_length=100)
    ville=models.CharField(max_length=100)
    pays=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom
    

class TypeVehicule(models.Model):
    nom=models.CharField(max_length=100)
    def __str__(self):
        return self.nom
    

class TailleVehicule(models.Model):
    nom=models.CharField(max_length=100)
    def __str__(self):
        return self.nom
    
    
class Vehicule(models.Model):
    type=models.ForeignKey(TypeVehicule,on_delete=models.CASCADE)
    date_created=models.DateField(default=date.today())
    prix=models.DecimalField(max_digits=6,decimal_places=2) 
    taille=models.ForeignKey(TailleVehicule,on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.nom
    
    
class Location(models.Model):
    date_location=models.DateField(default=date.today())
    date_retour=models.DateField(null=True,blank=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    vehicule=models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.client
    

class TarifLocation(models.Model):
    taux=models.DecimalField(max_digits=6,decimal_places=2)
    type_vehicule=models.ForeignKey(TypeVehicule,on_delete=models.CASCADE)
    taille_vehicule  =models.ForeignKey(TailleVehicule,on_delete=models.CASCADE)
    
        # def __str__(self):
        #     return self.taux
        