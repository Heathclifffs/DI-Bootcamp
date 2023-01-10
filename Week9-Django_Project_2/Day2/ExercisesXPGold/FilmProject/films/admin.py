from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pays,Categorie,Film,Directeur,Poste
# Register your models here.
class AdminPays(admin.ModelAdmin):
    list_display=['id','nom']
admin.site.register(Pays,AdminPays)
#.................................
class AdminCategorie(admin.ModelAdmin):
    list_display=['id','nom']
admin.site.register(Categorie,AdminCategorie)
#..........................................
class AdminDirecteur(admin.ModelAdmin):
    list_display=['id','nom','prenom']
admin.site.register(Directeur,AdminDirecteur)
#........................................
class AdminFilm(admin.ModelAdmin):
    list_display=['id','titre','date_sortie','film_nationalite','categorie']
admin.site.register(Film,AdminFilm)    
#...............................................
class AdminPoste(admin.ModelAdmin):
    list_display=['id','image']
admin.site.register(Poste,AdminPoste)