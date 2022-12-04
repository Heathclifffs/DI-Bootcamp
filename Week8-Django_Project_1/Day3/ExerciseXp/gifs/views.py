from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Gif
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .forms import GifForm,Category
# takes a request, returns a response

# index function renders homepage.html template

def Homepage(request):
    context = {
        'page_title': "Homepage",
        'gifs': Gif.objects.all()
    }
    return render(request, 'homepage.html', context)


def Addnewgif(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = GifForm(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
            form_uploader_name = form.cleaned_data['uploader_name']
            form_title = form.cleaned_data['title']
            form_URL = form.cleaned_data['URL']
            form_category = form.cleaned_data['category']

            context['formInfo'] = {
                    'uploader_name' : form_uploader_name,
                    'title': form_title,
                    'URL': form_URL,
                    'category ': form_category
                }
            print(context['formInfo'])
            return render(request, 'Add_gif.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'Add_gif.html', context)

    else:
        # GET, generate blank form
        context['form'] = GifForm()
    return render(request, 'add_new.html', context)


def Addnewcategory(request):
    context = {
        'page_title' : "Add",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = Category(request.POST) # the Person Form
        # check if it's valid:',
        if form.is_valid():
            form.save()
            form_name = form.cleaned_data['name']

            context['formInfo'] = {
                    'name' : form_name,

                }
            print(context['formInfo'])
            return render(request, 'Add_category.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'Add_category.html', context)

    else:
        # GET, generate blank form
        context['form'] = Category()
    return render(request, 'Add_category.html', context)


def categorys(request, id):
    context = {
        'id': id,
        'page_title': "Category",
        'gifs': Gif.objects.filter(id=id)
    }
    return render(request, 'category.html', context)

from .models import Category
def categories(request):
    context = {
        'page_title': "Category",
        'Categories': Category.objects.all()
    }
    return render(request, 'categories.html', context)

def Spegif(request, id):
    context = {
        'id': id,
        'page_title': "Gif",
        'gifs': Gif.objects.filter(id=id)
    }
    return render(request, 'SpeGif.html', context)
