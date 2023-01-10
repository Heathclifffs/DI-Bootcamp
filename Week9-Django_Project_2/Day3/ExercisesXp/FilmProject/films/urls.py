from django.urls import path
from films.views import add_film,add_director,home,edit_directeur,edit_film,add_poste,suprimer,add_commentaire,voir_commentaire


urlpatterns = [
    path('',home,name='homepage'),
    path('AddFilm',add_film,name='AddFilm'),
    path('AddDirector',add_director,name='AddDirector'), 
    path('edit_directeur/<int:id>',edit_directeur,name='editDirecteur'),
    path('edit_film/<int:id>',edit_film,name='editFilm'),
    path('AddPoste',add_poste,name='AddPoste'),
    path('suprimer/<int:id>',suprimer,name='suprimer'),
    path('commentaire/<int:id>',add_commentaire,name='commentaire'),
    path('voir_commentaire/<int:id>',voir_commentaire,name='voir_commentaire'),
               
  


  ]