
'''Exercice 4 : Date Actuelle
Des Instructions
Créez une fonction qui affiche la date actuelle.
Astuce : Utilisez le module datetime.'''
import datetime


def date():
    date=datetime.datetime.now()
    print(date)
date()