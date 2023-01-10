from django.urls import path
from films.views import add_film,add_director,home


urlpatterns = [
    path('',home,name='homepage'),
    path('AddFilm',add_film,name='AddFilm'),
    path('AddDirector',add_director,name='AddDirector'), 
               
  


  ]