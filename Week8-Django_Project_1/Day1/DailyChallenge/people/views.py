from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def index(request):
  template = loader.get_template('index.html')
  context={
    'people':people,
  }
  return HttpResponse(template.render(context, request))


def specific(request, id):
  template = loader.get_template('apeople.html')
  context = {
    'people':people,
     'id':id,
  }
  return HttpResponse(template.render(context, request))

