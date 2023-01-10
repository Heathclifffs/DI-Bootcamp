from django.contrib import admin
from .models import Image

# Register your models here.
class AdminImage(admin.ModelAdmin):
    list_display=['id','image','caption','uploader','date_created']
admin.site.register(Image,AdminImage)

