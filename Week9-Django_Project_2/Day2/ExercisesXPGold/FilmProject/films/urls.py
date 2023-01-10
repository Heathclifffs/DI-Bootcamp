from django.urls import path
from films.views import add_film,add_director,home,edit_directeur,edit_film,add_poste


urlpatterns = [
    path('',home,name='homepage'),
    path('AddFilm',add_film,name='AddFilm'),
    path('AddDirector',add_director,name='AddDirector'), 
    path('edit_directeur/<int:id>',edit_directeur,name='editDirecteur'),
    path('edit_film/<int:id>',edit_film,name='editFilm'),
    path('AddPoste',add_poste,name='AddPoste'),
               
  


  ]