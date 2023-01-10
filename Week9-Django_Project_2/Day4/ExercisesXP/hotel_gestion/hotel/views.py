from django.shortcuts import render
from .forms import AvisForm,ReservationForm,DeleteReservationForm,DeleteAvisForm,MessageForm,DeleteMessageForm
from . import forms
from django.contrib import messages
from hotel.models import Avis,Reservation,Chambre,Message,User,AbstractUser,Hotel
from django.contrib.auth.models import AbstractUser,User

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from . import models
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
# Create your views here.
def homepage(request):
    user = request.user
    if user.groups.filter(name='Personnel').exists():
        return redirect('all_reservation')
    else:
        hotel=Hotel.objects.all()
        context={
            'hotel':hotel
        }

    
    return render(request,'homepage.html',context)
#................................................

def editer_chambre(request,id):
    chambre=Chambre.objects.filter(id=id)
    return render(request,'utilisateur/reservation.html',{'chambre':chambre})

def all_reservation(request):
    reservation=Reservation.objects.all()
    context={
        'reservation':reservation
    }
    return render(request,'personnel/all_reservation.html',context)


#function ajout d'avis
@login_required
def add_avis(request):
    form=forms.AvisForm()
    if request.method=='POST':
        form= forms.AvisForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.author= request.user
            form.save()
            form=AvisForm()
            messages.success(request,'Avis ajoutez avec success!!!!')
            return redirect('voir_avis')
    return render(request,'utilisateur/avis.html',{'form':form})

def voir_avis(request):
    avis=Avis.objects.all().order_by('-created_on')
    context={
        'avis':avis
    }
    return render(request,'utilisateur/voir_avis.html',context)

def suprimer_avis(request,avis_id):
    avis=get_object_or_404(models.Avis,id=avis_id)
    avis.delete()
    messages.success(request,'Avis suprimer avec succes')
    return redirect('voir_avis')
   
#----------------------------------------FONCTIONS RESERVATIONS------------------------------
#..............faire une reservation
#fonction de resevation
@login_required
def reservation(request):
    reservation=Chambre.objects.all()
    context={
        'reservation':reservation
    }
    form= forms.ReservationForm()
    if request.method=='POST':
        form= forms.ReservationForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            # print(form.dure_sejour)
            dure_sejour=form.dure_sejour
            # print(form.reservation.prix)
            prix=form.reservation.prix
            form.prix_total=prix*dure_sejour
            # print(form.prix_total)
            form.author= request.user
            form.save()
            form=ReservationForm()
    return render(request,'utilisateur/reservation.html',{'form':form,'reservation':reservation})

#affiher tous les reservations
#..............modifier uune reservation....................................................
def editer_reservation(request,reservation_id):
    reservation=get_object_or_404(models.Reservation,id=reservation_id)
    edit_form= forms.ReservationForm(instance=reservation)
    delete_form= forms.DeleteReservationForm()
    user = request.user
    if request.method=='POST':
        if 'edit_reservation' in request.POST:
            edit_form= forms.ReservationForm(request.POST, instance=reservation)
            if edit_form.is_valid():
                p=edit_form.cleaned_data['dure_sejour']
                r=edit_form.cleaned_data['reservation']
                prix_total=p*r.prix
                reservation.prix_total=prix_total
                reservation.save()
                edit_form.save()
                if user.groups.filter(name='Personnel').exists():
                    messages.success(request,'Reservation modifier avec succes')
                    return redirect('all_reservation')
                else:
                    messages.success(request,'Reservation modifier avec succes')
                    return redirect('ma_reservation',request.user.id)
        if 'delete_reservation' in request.POST:
            delete_form= forms.DeleteReservationForm(request.POST)
            if delete_form.is_valid():
                reservation.delete()
                if user.groups.filter(name='Personnel').exists():
                    messages.success(request,'Reservation suprimer avec succes')
                    # return redirect('all_reservation')
                    return redirect('ma_reservation',request.user.id)

                else:
                    messages.success(request,'Reservation suprimer avec succes')
                    # return redirect('reservation')
                    return redirect('ma_reservation',request.user.id)

    context={
        'edit_form':edit_form,
    }   
    return render(request,'utilisateur/editer_Reservation.html',context=context)    

#------------------------reservation dun utilisateur
def ma_reservation(request,user_id):
    reservation=Reservation.objects.filter(author_id=user_id)
    context={
        'reservation':reservation
    }
   
    return render(request,'utilisateur/ma_reservation.html',context)    
    
#------------------------suprimer une reservation
def suprimer_reservation(request,reservationId):
    reservation=get_object_or_404(models.Reservation,id=reservationId)
    reservation.delete()
    messages.success(request,'Reservation suprimer avec succes')
    return redirect('ma_reservation',request.user.id)
#----------------------aficher tous les messages
def lesmessages(request):
    message=Message.objects.all()
    context={
        'message':message
    }
    return render(request,'utilisateur/messages.html',context)

#--------------------------------message demandant plus dinformations a lhotel
@login_required
def message(request):
    form=forms.MessageForm()
    if request.method=='POST':
        form= forms.MessageForm(request.POST)
        if form.is_valid():
            form= form.save(commit=False)
            form.author= request.user
            form.save()
            form=MessageForm()
            messages.success(request,'message envoyer avec success!!!!')
            return redirect('mes_messages',request.user.id)
    return render(request,'utilisateur/envoyer_message.html',{'form':form})
#----------------modifier le message
def modifier_message(request,message_id):
    message=get_object_or_404(models.Message,id=message_id)
    edit_form= forms.MessageForm(instance=message)
    delete_form= forms.DeleteMessageForm()
    if request.method=='POST':
        if 'edit_message' in request.POST:
            edit_form= forms.MessageForm(request.POST, instance=message)
            if edit_form.is_valid():
                            
                edit_form.save()
                messages.success(request,'message modifier avec succes')
                return redirect('mes_messages',request.user.id)
     
    context={
        'edit_form':edit_form,
    }  
    return render(request,'utilisateur/editer_message.html',context)
#--------------------supriner message----------------------------------------
def suprimer_message(request,message_id):
    message=get_object_or_404(models.Message,id=message_id)
    message.delete()
    messages.success(request,'message suprimer avec succes')
    return redirect('mes_messages',request.user.id)
   
#...................................................................................
def mes_messages(request,user_id):
    message=Message.objects.filter(author_id=user_id)
    # messages.success(request,'Aucun message')
    context={
        'message':message
    }
   
    return render(request,'utilisateur/mes_messages.html',context)    
    