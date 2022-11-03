# Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family:
    def __init__(self,last_name):
        self.last_name=last_name
        self.members=[]
        self.members=[{'name':'Michael','age':35,'gender':'Male','is_child':False},
                    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
                ]
        
    #method
    def born(self,**kargs):
        # n=newList["name"]+""+newList["age"]+""+newList["gender"]+""+newList["is_child"]
        self.members.append(kargs)
        # print(self.members)
        # print("")
    #method
    def is_18(self,name):
        for i in range(len(self.members)):
            for cle ,valeur in self.members[i].items():
                if name==valeur:  
                    m=self.members[i]
                    if m["age"]>18:
                
                        return True
                else:
                        return False        
    #method
    def family_presentation(self):
        for i in range(len(self.members)):
            
            m=self.members[i]
            # print(m["name"]+"--->"+self.last_name)

members_family=Family("Toure")    
members_family.born(name="el",
        age=12,
        gender="Male",
        is_child=True)
members=members_family.is_18('Michael')
members=members_family.is_18('Sarah')

print(members)
members_family.family_presentation()