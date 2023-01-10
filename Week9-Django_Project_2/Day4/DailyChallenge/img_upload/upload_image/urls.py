from django.urls import path
from upload_image.views import add_image,home

urlpatterns = [
    
    path('',home,name='homepage'),
    path('AddImage',add_image,name='AddImage'),

  ]