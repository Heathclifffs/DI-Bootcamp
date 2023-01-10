from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .forms import *
import time

# Create your views here.


def loginPage(request):
    
    page= 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username= request.POST.get('username').lower()
        password= request.POST.get('password')

        try:
            user = User.objects.get(username=username) 
        except:
            messages.error(request, 'Utilisteur non trouvee')

        user = authenticate(request,username=username, password=password)  

        if user is not None:
           login(request,user) 
           return redirect('home')
        else:
            messages.error(request,'Connection impossible')
            messages.error(request, 'Nom Utilisateur ou mot de passe incorect')


    context0={'page':page}
    return render(request, 'BookingRoom/login_register.html', context0)

def logoutUser(request):
    logout(request)
    return redirect('home')  

def registerUser(request):
    page='register'
    form= UserCreationForm()

    if request.method == 'POST' :
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home') 
        else:
            messages.error(request,' OOPS Une Erreur C\'est Produite')    

    return render(request, 'BookingRoom/login_register.html',{'form':form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    sections= Section.objects.filter(Q(sectionName__icontains=q))
    rooms= Room.objects.filter(
        Q(roomName__icontains=q)
        )
    context1= {'sections':sections,'rooms':rooms }
    return render(request,'BookingRoom/home.html',context1)

@login_required(login_url= 'login')
def room(request,pk):
    room= Room.objects.get(id=pk)
    movies= Movie.objects.all()
    plates= Plate.objects.all()
    chambers= Chamber.objects.all()
    restaus= Restauplace.objects.all()
    ResevR= ResevationPlate.objects.all()
    ResevC= ResevationChamber.objects.all()
    ticketCCount= ResevC.count()+1
    ticketRCount= ResevR.count()+1
    iroom=room

    if room.sectionId.sectionName == 'Restaurants':
        if request.method == 'POST':
            ticket = ResevationPlaceRestau.objects.create(
                roomName= iroom,
                # Created= datetime.date.now,
                Lieu= request.POST.get('Lieu'),
                Secteur= request.POST.get('Secteur'),
                Date= request.POST.get('Date'),
                Heure= request.POST.get('Heure'),
                Prix= request.POST.get('Prix'),
                Nom= request.POST.get('Nom'),
                Prenom= request.POST.get('Prenom'),
                Place= request.POST.get('Place')
            )
            if ticket:
                messages.warning(request, f'vous avez reserver un ticket pour {ticket.Heure} a {ticket.roomName.roomName} le {ticket.Date} ')
            else:    
                messages.error(request,' OOPS Une Erreur C\'est Produite') 

            return redirect('room', pk=room.id)

    context2={'room':room, 'movies':movies, 'plates':plates, 'chambers':chambers, 'restaus':restaus, 'ticketCCount':ticketCCount, 'ticketRCount':ticketRCount}
    return  render(request,'BookingRoom/rooms.html',context2)


def userProfil(request):
    user=request.user
    context= {}
    return render(request, 'BookingRoom/profil.html', context)


def section(request,pk):
    section= Section.objects.get(id=pk)
    rooms= Room.objects.all()
    context3= {'section':section, 'rooms':rooms}
    return render(request,'BookingRoom/section.html',context3)


@login_required(login_url= 'login')
def showMovie(request,pk):
    rooms= Room.objects.all()
    others= Movie.objects.all()
    resvations= ResevationMovie.objects.all()
    Resev= ResevationMovie.objects.all()
    movie= Movie.objects.get(id=pk)
    iroom=movie.roomName
    ticketCount= Resev.count()+1
    if request.method == 'POST':
        ticket = ResevationMovie.objects.create(
            roomName= iroom,
            # Created= datetime.date.now,
            Lieu= request.POST.get('Lieu'),
            Secteur= request.POST.get('Secteur'),
            MovieName=request.POST.get('MovieName'),
            Date= request.POST.get('Date'),
            Heure= request.POST.get('Heure'),
            Prix= request.POST.get('Prix'),
            Nom= request.POST.get('Nom'),
            Prenom= request.POST.get('Prenom'),
            Place= request.POST.get('Place')
        )
        if ticket:
            messages.warning(request, f'vous avez reserver un ticket pour {ticket.MovieName} ')
        else:    
            messages.error(request,' OOPS Une Erreur C\'est Produite') 

        return redirect('showMovie', pk=movie.id)

    context5= {'movie':movie,'rooms':rooms, 'others':others, 'ticketCount':ticketCount} 
    return render(request, 'BookingRoom/showMovie.html',context5)   

@login_required(login_url= 'login')    
def showPlate(request,pk):
    rooms= Room.objects.all()
    plate= Plate.objects.get(id=pk)
    Resev= ResevationPlate.objects.all()
    ticketCount= Resev.count() +1
    d= datetime.date.today()
    t= time.time
    print (t)
    iroom=plate.roomName

    if request.method == 'POST':
        ticket = ResevationPlate.objects.create(
            roomName= iroom,
            Lieu= request.POST.get('Lieu'),
            Secteur= request.POST.get('Secteur'),
            Plat=request.POST.get('PlateName'),
            Date= request.POST.get('Date'),
            Prix= request.POST.get('Prix'),
            Nom= request.POST.get('Nom'),
            Prenom= request.POST.get('Prenom'),
        )
        if ticket:
            messages.warning(request, f'vous avez reserver un ticket pour {ticket.Plat} ')
        else:    
            messages.error(request,' OOPS Une Erreur C\'est Produite') 

        return redirect('showPlate', pk=plate.id)
    context5= {'plate':plate, 'rooms':rooms, 'ticketCount':ticketCount, 'd':d,'t':t } 
    return render(request, 'BookingRoom/showPlate.html',context5)



def makeReservation(request):

    context4= {}
    return render(request,'BookingRoom/reservation_form.htm',context4)



def reservations(request):
    return render(request,'BookingRoom/reservation.html')

def userspace(request) :
    return render (request,'BookingRoom/userspace.html')   

@login_required(login_url= 'login')
def manageRoom(request,pk):
    
    room= Room.objects.get(id=pk)
    movies= Movie.objects.all()
    plates= Plate.objects.all()
    chambers= Chamber.objects.all()
    restaus= Restauplace.objects.all()
    ResevR= ResevationPlate.objects.all()
    ResevC= ResevationChamber.objects.all()
    form= RoomForm(instance=room)

    if request.user != room.roomHost:
        return HttpResponse('Vous Ne Devriez Pas Etre Ici ')

    if request.method == 'POST':
        form= RoomForm(request.POST,instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context= {'room':room, 'movies':movies, 'plates':plates, 'chambers':chambers, 'restaus':restaus, 'form':form}        
    return render(request,'BookingRoom/adminPannel.html',context)


@login_required(login_url= 'login')
def createMovie(request):

    form= MovieForm()
    if request.method == 'POST':
        form= MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'BookingRoom/movie_form.html', context)

@login_required(login_url= 'login')
def updateMovie(request,pk):
    movie= Movie.objects.get(id=pk)
    form= MovieForm(instance=movie)

    if request.method == 'POST':
        form=MovieForm(request.POST,instance=movie)
        if form.is_valid:
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request,'BookingRoom/movie_form.html',context)


@login_required(login_url= 'login')
def deleteMovie(request,pk):
    movie= Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'BookingRoom/delete.html',{'obj':movie})


@login_required(login_url= 'login')
def createPlate(request):
    form=PlateForm()
    if request.method == 'POST':
        form= PlateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'BookingRoom/plate_form.html', context)

@login_required(login_url= 'login')
def updatePlate(request,pk):
    plate= Plate.objects.get(id=pk)
    form= PlateForm(instance=plate)

    
    if request.method == 'POST':
        form=PlateForm(request.POST,instance=plate)
        if form.is_valid:
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request,'BookingRoom/movie_form.html',context)   

@login_required(login_url= 'login')
def deletePlate(request,pk):
    plate= Plate.objects.get(id=pk)
    if request.method == 'POST':
        plate.delete()
        return redirect('home')
    return render(request, 'BookingRoom/delete.html',{'obj':plate})     

@login_required(login_url= 'login')
def createChamber(request):
    form= ChamberForm()
    if request.method == 'POST':
        form= ChamberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'BookingRoom/chamber_form.html', context)

@login_required(login_url= 'login')
def updateChamber(request,pk):
    chamber= Chamber.objects.get(id=pk)
    form=ChamberForm(instance=chamber)

    if request.method == 'POST':
        form=ChamberForm(request.POST,instance=chamber)
        if form.is_valid:
            form.save()
            return redirect('home')
 
    context={'form': form}
    return render(request,'BookingRoom/movie_form.html',context) 

@login_required(login_url= 'login')
def deleteChamber(request,pk):
    movie= Chamber.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'BookingRoom/delete.html',{'obj':movie})       

@login_required(login_url= 'login')
def createRestauPlace(request):
    form= RestauForm()
    if request.method == 'POST':
        form= RestauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'BookingRoom/restau_form.html', context)

@login_required(login_url= 'login')
def deleteRestauPlace(request,pk):
    movie= Restauplace.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'BookingRoom/delete.html',{'obj':movie})    

@login_required(login_url= 'login')
def updateRestauPlace(request,pk):
    restau= Restauplace.objects.get(id=pk)
    form= RestauForm(instance=restau)

    if request.method == 'POST':
        form=RestauForm(request.POST,instance=restau)
        if form.is_valid:
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request,'BookingRoom/movie_form.html',context)    



@login_required(login_url= 'login')
def createRoom(request):
    form= RoomForm()

    if request.method == 'POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request,'BookingRoom/room_form.html', context)

@login_required(login_url= 'login')
def deleteRoom(request,pk):
    room= Room.objects.get(id=pk)
    if request.user != room.roomHost:
        return HttpResponse('Vous Ne Devriez Pas Etre Ici ')

    if request.method == 'POST': 
        room.delete()
        return redirect('home')
    return render(request, 'BookingRoom/delete.html',{'obj':room})