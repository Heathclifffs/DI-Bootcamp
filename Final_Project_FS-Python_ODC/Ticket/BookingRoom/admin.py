from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Section)
admin.site.register(Room)
admin.site.register(Plate)
admin.site.register(Chamber)
admin.site.register(Movie)
admin.site.register(Restauplace)
admin.site.register(ResevationMovie)
admin.site.register(ResevationChamber)
admin.site.register(ResevationPlaceRestau)
admin.site.register(ResevationPlate)
admin.site.register(Statut)
admin.site.register(Type)
admin.site.register(Wallet)