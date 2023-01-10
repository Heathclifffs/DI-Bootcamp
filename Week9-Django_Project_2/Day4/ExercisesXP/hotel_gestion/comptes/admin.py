from django.contrib import admin
from comptes.models import User
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display=('username','first_name','last_name','email','password','is_staff','is_active','date_joined')
admin.site.register(User,AdminUser)