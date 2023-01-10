from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Hotel,Chambre,Avis,User,Reservation,Message
# Register your models here.

class AdminHotel(admin.ModelAdmin):
    list_display=['id','nom','adresse','image','description']
admin.site.register(Hotel,AdminHotel)
#..............................................
class AdminAvis(admin.ModelAdmin):
    list_dipslay=['id','author','last_updated','created_on','published','content']
admin.site.register(Avis,AdminAvis)
#..................................................
class AdminChambre(admin.ModelAdmin):
    lisst_display=['id','date_disponible','date_reservation','prix','dure_sejour','nombre_personne','date_ariver','date_depart']
admin.site.register(Chambre,AdminChambre)
#.....................................
class AdminUser(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','password']
admin.site.register(User,AdminUser)
#..........................................
class AdminReservation(admin.ModelAdmin):
    list_display=['id','date_reservation','dure_sejour','author','reservation']
admin.site.register(Reservation,AdminReservation)
#..............................................
class AdminMessage(admin.ModelAdmin):
    list_display=['id','author','nom','email','content','date_envoi']
admin.site.register(Message,AdminMessage)