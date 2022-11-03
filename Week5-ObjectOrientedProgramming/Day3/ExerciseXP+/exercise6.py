
from datetime import date

def dateNaiss(date1,date2):
    n= (date2-date1).days
    min=n*1330
    return min
#date de user
date1= date(2001, 6, 12)
#calcul a partir de lannee actuelle
date2 = date(2022, 11, 3)
print("Vous avez vecu",dateNaiss(date1, date2), "minutes")    