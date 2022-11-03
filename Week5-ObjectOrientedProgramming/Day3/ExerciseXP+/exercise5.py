'''Temps Restant Jusqu'au 1er Janvier
Des Instructions
Créez une fonction qui affiche le temps restant jusqu'au 1er janvier.
( Exemple : le 1er janvier est dans 10 jours et 10:34:01heures).'''
from datetime import date

def temps(date1,date2):
    n= (date1-date2).days
    return n
#date de user
date1= date(2023, 1, 1)
#calcul a partir de lannee actuelle
date2 = date(2022, 11, 3)
print("IL reste",temps(date1, date2), "jours pour atteindre le 1er janvier")    