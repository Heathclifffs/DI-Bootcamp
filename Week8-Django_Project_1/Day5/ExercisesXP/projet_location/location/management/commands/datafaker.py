from django.core.management.base import BaseCommand
from faker import Faker
from location.models import Client
class Command(BaseCommand):
    help="Command information"
    
    def handle():
        faker= Faker()

        for i in range(10):
            prenom=faker.first_name()
            nom=faker.last_name()
            email=faker.email()
            numero=faker.phone_number()
            adresse=faker.address()
            ville=faker.city()
            pays=faker.country()
            
            client=Client.objects.create(prenom=prenom,nom=nom,email=email,numero=numero,adresse=adresse,ville=ville,pays=pays)
            client.save()
        return client
            # print(faker.first_name())
    handle()
#faker locations
# def locations():
#     faker=Faker()