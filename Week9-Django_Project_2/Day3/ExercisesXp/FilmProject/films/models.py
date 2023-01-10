from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date
from django.conf import settings

# Create your models here.
class Pays(models.Model):
    nom=models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    
#.....................................
class Categorie(models.Model):
    nom=models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    
#...................................
class Directeur(models.Model):
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom
    
#.....................................
#........................................
class Poste(models.Model):
    image=models.ImageField(upload_to='Images',blank=True)
    
#..................................
class Commentaire(models.Model):
    author = models.ForeignKey('comptes.User', on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    
    def __str__(self):
        return self.content
#.....................................................
class Film(models.Model):
    titre=models.CharField(max_length=30)
    date_sortie=models.DateField(default=date.today())
    film_nationalite=models.ForeignKey(Pays,on_delete=models.CASCADE)
    pays_disponible=models.ManyToManyField(Pays,related_name='pays_disponible_film')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    realisateurs=models.ManyToManyField(Directeur)
    afficher=models.OneToOneField(Poste,on_delete=models.CASCADE)
    commentaire=models.ManyToManyField(Commentaire)
  
    def __str__(self):
        return self.titre
    

    
    