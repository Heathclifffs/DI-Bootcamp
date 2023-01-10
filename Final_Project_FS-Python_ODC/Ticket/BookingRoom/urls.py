from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
     path('register/', views.registerUser, name='register'),
    path('profil/', views.userProfil, name='user-profil'),
    path('admin/<str:pk>/', views.manageRoom, name='admin'),


    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('reservation/', views.reservations, name='reservation'),
    path ('userspace/', views.userspace, name='userspace'),
    path('section/<str:pk>/', views.section, name='section'),
    path ('showMovie/<str:pk>/', views.showMovie, name='showMovie'),
    path ('showPlate/<str:pk>/', views.showPlate, name='showPlate'),
    path('make-reservation/', views.makeReservation, name='make-reservation'),

    path('create-room/',views.createRoom,name='create-room'),
    # path('update-room',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    
    path('create-movie/',views.createMovie,name='create-movie'),
    path('update-movie/<str:pk>',views.updateMovie,name='update-movie'),
    path('delete-movie/<str:pk>',views.deleteMovie,name='delete-movie'),

    path('create-plate',views.createPlate,name='create-plate'),
    path('update-plate/<str:pk>',views.updatePlate,name='update-plate'),
    path('delete-plate/<str:pk>',views.deletePlate,name='delete-plate'),
    

    path('create-chamber',views.createChamber,name='create-chamber'),
    path('update-chamber/<str:pk>',views.updateChamber,name='update-chamber'),
    path('delete-chamber/<str:pk>',views.deleteChamber,name='delete-chamber'),

    path('create-restau',views.createRestauPlace,name='create-restau'),
    path('update-restau/<str:pk>',views.updateRestauPlace,name='update-restau'),
    path('delete-restau/<str:pk>',views.deleteRestauPlace,name='delete-restau'),
]