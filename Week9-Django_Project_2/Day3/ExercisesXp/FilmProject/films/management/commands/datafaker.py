from django.core.management.base import BaseCommand
from faker import Faker
from films.models import Pays,Categorie,Directeur,Film
#...............................................
class Command(BaseCommand):
    help="Command information"
    
    def handle():
        faker= Faker()
        
        for i in range(7):
            pays=faker.country()
            prenom=faker.first_name()
            nom=faker.last_name()
            p=Pays.objects.create(nom=pays)
            d=Directeur.objects.create(nom=nom,prenom=prenom)
            p.save()
            d.save()
    handle()