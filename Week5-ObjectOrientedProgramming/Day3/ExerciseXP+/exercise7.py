from datetime import date
import datetime
def dateVac(date1,date2):
    d=(date1-date2).days
    heure=219*24
    second=86400*219
    minutes=d*1440
    return "{} jours et dans {}h:{}m:{}s".format(d,heure,minutes,second,"secondes")  
#apel de la fonction
y=datetime.datetime.now().year
m=datetime.datetime.now().month
d=datetime.datetime.now().day  
date1=date(2023,5,1)    
date2=date(y,m,d)
print("Les prochains vacances sont dans :",dateVac(date1,date2))