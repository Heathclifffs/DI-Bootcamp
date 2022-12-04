from django.contrib import admin
from  .models import Gif,Category

# Register your models here.
class AdminGif(admin.ModelAdmin):
    list_display = ('id','title','URL','uploader_name','created_at')

class AdminCategory(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Gif,AdminGif)
admin.site.register(Category,AdminCategory)

