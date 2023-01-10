from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ImageForm
from upload_image.models import Image
from . import forms

from . import models
from django.contrib import messages

# Create your views here.
def home(request):
    image=Image.objects.all().order_by('-date_created')
    context={
    'image':image
    }
    return render(request,'homepage.html',context)
#...................................................

#..........................................................
def add_image(request):
    form= forms.ImageForm()
    if request.method=='POST':
        form= forms.ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.uploader=request.user
            form.save()
            form=ImageForm()            
            messages.success(request, 'Image ajoutez avec succes') # ignored
            return redirect('homepage')
    return render(request,'image/add_image.html',{'form':form})