from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client,TailleVehicule,TypeVehicule,Vehicule,Location,TarifLocation
# Register your models here.
class AdminClient(admin.ModelAdmin):
    list_display=('id','nom','prenom','email','numero','adresse','ville','pays')
admin.site.register(Client,AdminClient)
#......................................................
#type vehicule
class AdminTypeVehicule(admin.ModelAdmin):
    list_display=('id','nom')
admin.site.register(TypeVehicule,AdminTypeVehicule)
#...................................................
#taille vehicule
class AdminTailleVehicule(admin.ModelAdmin):
    list_display=('id','nom')
admin.site.register(TailleVehicule,AdminTailleVehicule)
#.......................................................
#vehicule
class AdminVehicule(admin.ModelAdmin):
    list_display=('id','type','date_created','prix','taille')
admin.site.register(Vehicule,AdminVehicule)
#.................................................
#location
class AdminLocation(admin.ModelAdmin):
    list_display=('id','date_location','date_retour','client','vehicule')
admin.site.register(Location,AdminLocation)
#....................................................................
#tarif de location
class AdminTarifLocation(admin.ModelAdmin):
    list_display=('id','taux','type_vehicule','taille_vehicule')
admin.site.register(TarifLocation,AdminTarifLocation)