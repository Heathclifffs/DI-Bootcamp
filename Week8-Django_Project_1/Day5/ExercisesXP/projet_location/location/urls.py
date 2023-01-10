from django.urls import path
from location.views import home,add_location,location,detail_location,afficher_clients,ajout_client,ajout_vehicule

urlpatterns = [
    path('',home,name='home'),
    path('location/add',add_location,name='add_location'),
    path('location',location,name='location'),
    path('location/<int:id>',detail_location,name='detail_location'),
    path('clients',afficher_clients,name='client'),
    path('ajout_client',ajout_client,name='ajout_client'),
    path('ajout_vehicule',ajout_vehicule,name='ajout_vehicule'),
]