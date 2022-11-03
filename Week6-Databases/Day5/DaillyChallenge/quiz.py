# Part 1 : Quizz :
# Répondre aux questions suivantes

# Qu'est-ce qu'une classe ?
# Qu'est-ce qu'une instance ?
# Qu'est-ce que l'encapsulation ?
# Qu'est-ce que l'abstraction ?
# Qu'est-ce que l'héritage ?
# Qu'est-ce que l'héritage multiple ?
# Qu'est-ce que le polymorphisme ?
# Qu'est-ce que l'ordre de résolution de méthode ou MRO ?


# Partie 2 : Créer Une Classe De Jeu De Cartes.
# La Deckclasse of cards ne doit PAS hériter d'une Cardclasse.

# Les exigences sont les suivantes :

# La Cardclasse doit avoir une couleur (cœur, carreau, trèfle, pique) et une valeur (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# La Deckclasse :
# devrait avoir une shuffleméthode qui s'assure que le jeu de cartes contient les 52 cartes, puis les réorganise de manière aléatoire.
# devrait avoir une méthode appelée dealqui distribue une seule carte du jeu. Une fois qu'une carte a été distribuée, elle doit être retirée du paquet.
#-------------------------------------------------------------------------------------
                        #QUIZZ

# une classe est une representation dun objet 

# une instance est un objet d'une classe

#l'abstraction consiste a cacher les donnees inutiles a lutilisateur

# l'heritage cest lorsqune classe herite des attributs et methodes dune classe superieur(class mere)

# l'heritage multiple c'est lorsqune classe herite dune class mere et que une autre class
# herite de la classe qui herite la classe mere

# le polymorphisme est la capacité d’une fonction (ou méthode) à se comporter différemment en fonction
# de l’objet qui lui est passé.

# le MRO C'est l'ordre dans lequel une méthode est recherchée dans une hiérarchie de classe
# En Python, le MRO est de bas en haut et de gauche à droite.
# Cela signifie que, d'abord, la méthode est recherchée dans la classe de l'objet. 
# S'il n'est pas trouvé, il est recherché dans la super classe immédiate.
# Dans le cas de plusieurs super classes, il est recherché de gauche à droite,
# dans l'ordre dans lequel il a été déclaré par le développeur. 
import queue
from random import randint
import random
from collections import deque
class Card:
    def __init__(self):
        self.liste=[]
        self.couleur=['coeur','carreau','trefle','pique']
        self.valeur=['A','2', '3','4','5','6','7','8','9','10','J','Q', 'K']
        for i in range(1,52):
            self.liste.append(i)
        # print(self.liste)
    #methode
class Deck():
    def __init__(self):
        self.liste=[]
        for i in range(1,52):
            self.liste.append(i)
    #method
    def aleatoire(self): 

        random.shuffle(self.liste)
        # print(self.liste)
    #method
    def deal(self):
        joueur1=[]
        joueur2=[]
        # d=deque()
        # self.aleatoire()
        taille=len(self.liste)
        # print(self.liste)
        t=1
        while t!=0:
            if self.liste:
                
                # print("sssss:",self.liste)
                carte =random.randint(1,taille-1)
                if carte in self.liste:
                    
                    joueur1.append(carte)
                    index=self.liste.index(carte)
                # self.liste.pop(carte)
                    self.liste.pop(index)
                    print("ON a retirre :",carte)
                    print("New list :",self.liste)
                    taille=len(self.liste)
                    print("taill dvient :",taille)
                # else:
                #     continue    

                carte2 =random.randint(1,taille)
                if carte2 in self.liste:
                    
                    joueur2.append(carte2)
                    index2=self.liste.index(carte2)
                    self.liste.pop(index2)
                    print("ON a retirre :",carte2)
                    print("New list :",self.liste)
                    taille=len(self.liste)
                    print("taill dvient :",taille)
                # else:
                #     continue
            else:
                print("liste vide")
                break
            # self.liste.pop(carte2)
                 
                # print(self.liste)
                # break
            # print(self.liste)    
        print("carte j1 :",joueur1)
        print("carte 2: ",joueur2)    
        
#instance
card=Card()       
deck=Deck()
deck.aleatoire()
deck.deal()