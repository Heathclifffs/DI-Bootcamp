from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Animal,Family

# Create your views here.
def family(request, id):
    template=loader.get_template('familly.html')
    context = {
        'Animal': Animal.objects.all().values(),
        'Family': Family.objects.all().values(),
        'id': id,

    }
    return HttpResponse(template.render(context, request))


def animal(request, id):
    template=loader.get_template('animal.html')

    context = {
        'Animal': Animal.objects.all().values(),
        'Family': Family.objects.all().values(),
        'id': id,

    }
    return HttpResponse(template.render(context, request))



def animals(request):
    template=loader.get_template('animals.html')

    context = {
        'Animal': Animal.objects.all(),
        'Family': Family.objects.all(),
        'id': id,

    }
    return HttpResponse(template.render(context, request))


