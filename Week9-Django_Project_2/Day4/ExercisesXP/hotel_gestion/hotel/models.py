from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date,datetime
from django.conf import settings

# Create your models here.
class Hotel(models.Model):
    nom=models.CharField(max_length=30,default='Tork-kee')
    adresse=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Images',blank=True)
    description=models.TextField()
    
    
    def __str__(self):
        return self.nom
#..................................................................
class Avis(models.Model):
    author = models.ForeignKey('comptes.User', on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(default=datetime.today())
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    def __str__(self):
        return self.content 
    
class Message(models.Model):
    author = models.ForeignKey('comptes.User', on_delete=models.SET_NULL, null=True, blank=True)
    nom=models.CharField(max_length=30)
    email=models.EmailField()
    content=models.TextField(blank=True,verbose_name="Contenu")
    date_envoi=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

    
#...................................................
class Chambre(models.Model):
    date_disponible=models.DateField(blank=True,null=True)
    prix=models.DecimalField(max_digits=7,decimal_places=2)
    nombre_personne=models.IntegerField()
    date_ariver=models.DateField(blank=True,null=True)
    date_depart=models.DateField(blank=True,null=True)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    disponible=models.BooleanField(default=False)
    occupe=models.BooleanField(default=False)

    
    # def __str__(self):
    #     return self.content 
#...............................................................
class Reservation(models.Model):
    date_reservation=models.DateTimeField(default=datetime.today())
    dure_sejour=models.IntegerField()
    author = models.ForeignKey('comptes.User', on_delete=models.SET_NULL, null=True, blank=True)
    reservation=models.ForeignKey(Chambre,on_delete=models.CASCADE)
    prix_total=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)


