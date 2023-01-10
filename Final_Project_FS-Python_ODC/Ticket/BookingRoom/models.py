from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from os import *
import os
from pathlib import Path
import datetime

# Create your models here.

BASE_DIR = Path(__file__).resolve().parent.parent

class Section(models.Model):
    sectionName= models.CharField(max_length=200)
    sectionUpdated= models.DateTimeField(auto_now=True)
    SectionCreated= models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.sectionName)

class Statut (models.Model):
    status= models.CharField(max_length=50)

    def __str__(self):
        return self.status        

class Type (models.Model):
    type= models.CharField(max_length=50)

    def __str__(self):
        return self.type        

class Room(models.Model):
    roomName= models.CharField(max_length=200)
    roomHost= models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    sectionId= models.ForeignKey(Section, on_delete=models.SET_NULL,null=True)
    roomCreated= models.DateTimeField(auto_now_add=True)
    roomUpdated= models.DateTimeField(auto_now=True)
    roomDesc= models.TextField(null=True)
    roomPlaceAvailabe= models.IntegerField(null=False,default=0)
    roomPicture= models.ImageField(upload_to='BookingRoom/templates/roomPictures',blank=True, null=True)
    roomOpenHour= models.TimeField(default='19:30:00')
    roomCloseHour= models.TimeField(default='02:00:00')
    roomPlace= models.CharField(max_length=200,default='Ouagadougou')
    roomGeoLoc= models.CharField(max_length=200, default='Pissy' )
    roomOpenDay= models.CharField(max_length=200,default='Lundi-Dimanche') 
    #roomRate=
    class Meta:
        ordering = ['-roomUpdated', '-roomCreated']

    def __str__(self):
        return str(self.roomName)


class Movie(models.Model):
    movieName= models.CharField(max_length=200)
    movieDesc= models.TextField(null=True)
    movieDuration= models.IntegerField(null=False, default=154)
    movieLanguage= models.CharField(max_length=200, default='Unknow')
    movieCreator= models.CharField(max_length=200, default='Unknow')
    moviePicture= models.ImageField(upload_to='BookingRoom/templates/moviePictures',blank=True, null=True)
    movieDiffDate= models.DateField(default='2023-01-01')
    movieDiffHour= models.TimeField(default='00:00:00')
    #movieRate=
    movieType=models.CharField(max_length=200,default='Cinema-Aventure-SF')
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    movieUpdated= models.DateTimeField(auto_now=True)
    movieCreated= models.DateTimeField(auto_now_add=True)
    movieTotalplace= models.IntegerField
    movieAvailableplaces=models.IntegerField(null=False,default=24)
    movieTicketPrice= models.IntegerField(null=False,default=1500)
    movieStatus= models.ForeignKey(Statut, on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['-movieUpdated', '-movieCreated']

    def __str__(self):
        return str(self.movieName) 


class Plate(models.Model):
    plateName= models.CharField(max_length=200)
    plateDesc= models.TextField(null=True)
    plateIngredient = models.TextField(default='secret')
    platePicture= models.ImageField(upload_to='BookingRoom/templates/platePictures',blank=True, null=True)
    #plateRate=
    plateCooker= models.CharField(max_length=200, default='Unknow')
    plateType= models.CharField(null=False, default='Plat', max_length=200) 
    roomName= models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    plateTicketPrice= models.IntegerField(null=False,default=1500)
    PlateCreated= models.DateTimeField(auto_now_add=True)
    PlateUpdated= models.DateTimeField(auto_now=True)
    PlateMinCookTime= models.IntegerField(null=False,default=60)
    PlateStatus= models.ForeignKey(Statut, on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering = ['-PlateUpdated', '-PlateCreated']

    def __str__(self):
        return str(self.plateName)

class Restauplace(models.Model):
    restauUpdated= models.DateTimeField(auto_now=True)
    restauCreated= models.DateTimeField(auto_now_add=True)
    restauTotalplace= models.IntegerField(null=False,default=60)
    restauAvailableplaces=models.IntegerField(null=False,default=60)
    restauTicketPrice= models.IntegerField(null=False,default=1500)
    roomName= models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return str(self.restauAvailableplaces)


class Chamber(models.Model):
    chamberNum= models.IntegerField(null=False,default=0)
    chamberPicture= models.ImageField(upload_to='BookingRoom/templates/chamberPictures',blank=True, null=True)
    chamberDesc= models.TextField(null=True)
    chamberType= models.ForeignKey(Type, on_delete=models.SET_NULL,null=True)
    ChamberStatus= models.ForeignKey(Statut, on_delete=models.SET_NULL,null=True)
    #chamberRated=
    chamberUpdated= models.DateTimeField(auto_now=True)
    chamberCreated= models.DateTimeField(auto_now_add=True)
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    chamberTicketPrice= models.IntegerField(null=False,default=1500)

    def __str__(self):
        var=f'{self.roomName.roomName} | Type:{self.chamberType}'
        return var

class ResevationMovie(models.Model):
    section='cinema'
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    Lieu= models.CharField(max_length=200)
    Secteur= models.CharField(max_length=200)
    MovieName= models.CharField(max_length=200)
    Date= models.DateField()
    Heure= models.TimeField()
    Prix= models.IntegerField()
    Nom= models.CharField(max_length=200)
    Prenom= models.CharField(max_length=200)
    Place= models.IntegerField() 
    Created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        var=[self.MovieName,self.roomName,self.section]
        return str(var)
    

class ResevationPlate(models.Model):
    section='Restaurant'
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    Lieu= models.CharField(max_length=200)
    Secteur= models.CharField(max_length=200)
    Plat= models.CharField(max_length=200)
    Date= models.DateField()
    Prix= models.IntegerField()
    Nom= models.CharField(max_length=200)
    Prenom= models.CharField(max_length=200)
    Created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        var=[self.Plat,self.roomName,self.Date,self.section]
        return str(var)
# 
class ResevationPlaceRestau(models.Model):
    section='Restaurant'
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    Lieu= models.CharField(max_length=200)
    Secteur= models.CharField(max_length=200)
    Date= models.DateField()
    Heure= models.TimeField()
    Prix= models.IntegerField()
    Nom= models.CharField(max_length=200)
    Prenom= models.CharField(max_length=200)
    Place= models.IntegerField() 
    Created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        var=[self.Date,self.Heure,self.roomName,self.section]
        return str(var)




class ResevationChamber(models.Model):
    section='Hotel'
    roomName= models.ForeignKey(Room, on_delete=models.SET_NULL,null=True)
    chamberNum= models.ForeignKey(Chamber, on_delete=models.SET_NULL,null=True)
    #heure=
    #mail
    #plateTicketPrice=
    #numReservation=
    #user
    def __str__(self):
        var=[self.chamberNum,self.roomName,self.section]
        return str(var)

# class T(models.Model):
    # time= models.DateTimeField()


class Wallet(models.Model):
    value= models.FloatField(default=0.0)
    user= models.ForeignKey(User, on_delete=CASCADE)