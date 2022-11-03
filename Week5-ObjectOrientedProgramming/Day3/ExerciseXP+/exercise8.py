''' Exercice 8 : Quel Âge As-Tu Sur Jupiter ?
 Des Instructions
 Étant donné un âge en secondes, calculez l'âge que quelqu'un aurait sur :
Terre : période orbitale 365,25 jours terrestres ou 31557600 secondes
Mercure : période orbitale 0,2408467 années terrestres
Vénus : période orbitale 0,61519726 années terrestres
Mars : période orbitale 1,8808158 années terrestres
Jupiter : période orbitale 11,862615 années terrestres
Saturne : période orbitale 29,447498 années terrestres
Uranus : période orbitale 84,016846 années terrestres
Neptune : période orbitale 164,79132 années terrestres
Donc, si on vous dit que quelqu'un a 1 000 000 000 de secondes, la fonction devrait indiquer qu'il a 31,69 années terrestres.
'''
def age(n):
    terre=(n*365.25)/ 31557600
    ann=terre/365
    print("Terre {} annees terrestres".format(ann))
    mercure= 0.2408467*ann
    print("Mercure {} annees terrestres".format(mercure))
    venus=ann*0.61519726 
    print("Venus{} annees terrestres".format(venus))
    mars=ann*1.8808158
    print("Mars{} annees terrestres".format(mars))
    jupiter=ann* 11.862615 
    print("Jupiter{} annees terrestres".format(jupiter))
    saturne=ann*29.447498
    print("Saturne {} annees terrestres".format(saturne))
    uranus=ann*84.016846 
    print("Uranus {} annees terrestres".format(uranus))
    neptune=ann*164.79132
    print("Neptune {} annees terrestres".format(neptune))

    
age(1000000000)