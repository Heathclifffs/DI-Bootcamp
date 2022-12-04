from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Person

# Create your views here.
def phonenumber(request, phonenumber):
    template=loader.get_template('phonenumber.html')
    data=Person.objects.filter(phone_number=phonenumber).values()

    context = {
        'Person':data,
        'pn':phonenumber,
    }
    return HttpResponse(template.render(context, request))

def name(request, name):
    data=Person.objects.filter(name=name).values()
    template=loader.get_template('name.html')
    context = {
        'Person':data,
        'n':name,

    }
    return HttpResponse(template.render(context, request))
