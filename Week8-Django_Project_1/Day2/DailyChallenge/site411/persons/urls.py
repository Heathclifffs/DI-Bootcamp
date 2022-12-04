from django.urls import path
from . import views

urlpatterns = [
    path('<int:phonenumber>', views.phonenumber, name='phonenumber'),
    path('<str:name>/', views.name, name='name'),
]