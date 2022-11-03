# TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:

# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]


# 2.Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.


# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

from Exercise1 import Family

class TheIncredibles(Family):
    def __init__(self,last_name):
        self.members=[]
        self.memberss=[
                        {'name':'Michael','age':33,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
                    ]
        super().__init__(last_name)
        
    #method
    def use_power(self,name):
        try:
            
            for i in range(len(self.memberss)):
                for cle ,valeur in self.memberss[i].items():
                    if name==valeur:  
                     m=self.members[i]
                    if m["age"]>18:
                
                        return m["name"]+"-->power "+m["power"]
                    else:
                        return False
        except:          
            print("They are not over 18 years old")
    #method
    # def incredible_presentation(self):
    #         for i in range(len(self.memberss)):
    #             m=self.memberss[i]
    #             print(m["power"],end=" ")
    #             return super(TheIncredibles,self).family_presentation()
        
            
incredible=TheIncredibles("Traore")
members=incredible.use_power('Michael')
# members=incredible.use_power('Sarah')

print(members)
#incredible presentation
inc_present=incredible.incredible_presentation()
print(inc_present)