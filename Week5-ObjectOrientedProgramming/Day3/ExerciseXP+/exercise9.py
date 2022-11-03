# Exercice 9 : Module Faker
# Des Instructions
# Installez le module faker , consultez la documentation et apprenez à implémenter correctement faker dans votre code.
# Créez une liste vide appelée users. Astuce : Il doit s'agir d'une liste de dictionnaires.
# Créez une fonction qui ajoute de nouveaux dictionnaires à la usersliste. Chaque utilisateur dispose des clés suivantes : nom , adresse , code_langue . Utilisez faker pour les remplir avec de fausses données.
from faker import Faker
def ajout(dico):
    users=[]
    users.append(dico)
    return users
    

fake=Faker()
dico=dict()
for i in range(1):
    dico["nom"]=fake.name()    
    dico["adresse"]=fake.address()
    # dico["code_langue"]=fake.language()
print(ajout(dico))