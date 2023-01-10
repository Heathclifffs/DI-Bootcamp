from django.shortcuts import render
# from . import forms
from .forms import ClientForm,VehiculeForm,ClientAddForm,VehiculeAddForm
from .models import Client,Vehicule,TailleVehicule,TypeVehicule,Location,TarifLocation
from django.contrib import messages
from django.contrib.postgres.search import SearchVector
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
# Create your views here.
def home(request):
   
    return render(request,'home.html')
#.............................................................
def location(request):
    location=Location.objects.filter(date_retour__isnull=True).order_by('date_retour')
    # locations=Location.objects.filter(date_retour__isnull=False).order_by('date_retour')
    

    context={
        'location':location
    }
    return render(request,'location/location.html',{'location':location})
#.........................................................
def detail_location(request,id):
    client=Location.objects.filter(vehicule_id=id)
    context={
        'client':client,
    }
    return render(request,'location/detail_location.html',context)
#........................................................................
def add_location(request):
    formVehicule=VehiculeForm()
    formClient=ClientForm()

    if request.method=='POST':
        formClient=ClientForm(request.POST)
        formVehicule=VehiculeForm(request.POST)
        if formClient.is_valid() and formVehicule.is_valid():
            prenom=formClient.cleaned_data['prenom']
            type=formVehicule.cleaned_data['type']
            print("prenon saisie dans le formulaire--------------->",prenom)
            print("type de vehicule saisie dans le formulaire----->",type)
            try:
                TypeVehicule.objects.get(nom=type)
                id=TypeVehicule.objects.get(nom=type)
                id=Vehicule.objects.get(type_id=id.id)
                nom=id
                id_client=Client.objects.get(prenom=prenom)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "ce vehicule n\'existe  pas dans la base de donee")

          
            if Client.objects.filter(prenom=prenom):
                if  TypeVehicule.objects.filter(nom=type):
                    if Location.objects.filter(vehicule_id=nom.id,date_retour__isnull=True):
                        
                    
                        messages.add_message(request, messages.INFO, 'ce vehicule est en location')

                       
                    else:
                        location=Location.objects.create(vehicule_id=nom.id,client_id=id_client.id)
                        location.type=type
                        location.prenom=prenom
                       
                        location.save()
                        messages.add_message(request, messages.SUCCESS, 'Location creee avec succes')

                        
                else:
                   messages.add_message(request, messages.INFO, "ce vehicule n\'existe  pas dans la base de donee")

            else:
                messages.add_message(request, messages.INFO, "ce nom n\'existe pas")


    
    return render(request,'forms/add_location.html',{'formClient':formClient,'formVehicule':formVehicule})
#affichage de tous les clients par ordre alphabetique
def afficher_clients(request):
    clients=Client.objects.all().order_by('nom')
    context={
        'clients':clients
    }
    return render(request,'Clients/client.html',context)
#......................................................................
def ajout_client(request):
    form_add_client=ClientAddForm()
    if request.method=='POST':
        form_add_client=ClientAddForm(request.POST)
        if form_add_client.is_valid():
            form_add_client= form_add_client.save(commit=False)

            form_add_client.save()
            form_add_client=ClientAddForm()
            
    return render(request,'Clients/ajout_client.html',{'form':form_add_client})
#.......................................................................
def afficher_vehicule(request):
    vehicule=Vehicule.objects.all(type_id=id,taille_id=id)
    context={
        'vehicule':vehicule
    }
    
#.........................................
def ajout_vehicule(request):
        form_add_vehicule=VehiculeAddForm()
        if request.method=='POST':
            form_add_vehicule=VehiculeAddForm(request.POST)
            if form_add_vehicule.is_valid():
                type=form_add_vehicule.cleaned_data['nom']
                print(type)
                nom=TypeVehicule.objects.create(nom=type)
                prix=form_add_vehicule.cleaned_data['prix']
                taille=form_add_vehicule.cleaned_data['taille']

                if TailleVehicule.objects.filter(nom=taille):
                    id_taille=TailleVehicule.objects.get(nom=taille)
                    print(id_taille)
                    nouveau_vehicule=Vehicule.objects.create(type=nom,prix=prix,taille_id=id_taille.id)

                    nouveau_vehicule.save()
                    nouveau_vehicule=VehiculeAddForm()
                    messages.add_message(request, messages.SUCCESS, 'Location creee avec succes')
                else:
                    nouveau_taille=TailleVehicule.objects.create(nom=taille)
                    nouveau_vehicule=Vehicule.objects.create(type=nom,prix=prix,taille_id=nouveau_taille.id)

                    nouveau_vehicule.save()
                    nouveau_vehicule=VehiculeAddForm()
                    messages.add_message(request, messages.SUCCESS, 'Location creee avec succes')


                    
        return render(request,'vehicule/ajout_vehicule.html',{'form':form_add_vehicule})