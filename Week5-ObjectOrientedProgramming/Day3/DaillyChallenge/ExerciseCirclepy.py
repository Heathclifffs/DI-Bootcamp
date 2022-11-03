''' Instructions :The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.
Other abilities of a Circle instance:Compute the circle’s area
Print the circle and get something nice
Be able to add two circles together
Be able to compare two circles to see which is bigger
Be able to compare two circles and see if there are equal
Be able to put them in a list and sort them
'''

class Circle:
    def __init__(self,rayon,diametre):
        self.rayon=rayon
        self.diametre=diametre
        liste=[]
        self.liste=liste
        
    #method
    def aire(self):
        return "Area of the circle est {}".format(3.14*self.rayon*self.rayon)    
    #method
    def __eq__(self,other):
        self.liste.append(self.rayon)
        self.liste.append(self.diametre)
        self.liste.append(other.rayon)
        self.liste.append(other.diametre)
        self.liste.sort()
        print("Liste trier:",self.liste)
        if self.rayon*2*3.14==other.rayon*2*3.14:
            
            print(self.liste)
            return "the two circle are the sames"
        elif self.rayon*2*3.14 >other.rayon*2*3.14:
            
            return "Thefirst one is the bigest one"

        else:
            return "the second circle is the biggest one "
    #methos
    def __repr__(self,other):
        return f"{self.__class__.__name__} : {self.rayon*2*3.14+other.rayon*2*3.14}"

    #method
   
        
        
        
        
c1=Circle(4,10)      
c2=Circle(5,20)  
print(c1.aire())
print(c1.__eq__(c2))
print(c1.__repr__(c2))
