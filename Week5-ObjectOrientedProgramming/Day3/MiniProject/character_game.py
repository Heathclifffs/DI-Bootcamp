# Mini-Project: Characters Game
'''Description
Create a class called Character with the following attributes and methods:
attribute name
attribute life – starts with a default value of 20
attribute attack – the base attack of a character (integer) will be a default of 10
method basic_attack() - accepts another Character instance as a parameter. Your character will <attack> the other character so his <life> points should drop.'''

'''Instructions
Now create 3 different classes that inherit from Character:
Every character type should say (ie. print) something when they are created, get creative :)
Druid:
meditate() - increases life by 10, decrease attack by 2
animal_help()- increases attack by 5
fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other character’s life.
Example:
druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)'''

'''Warrior:
brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
train() - increases both your attack and life points by 2.
roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.'''

'''Mage:
curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
summon() - increases attack attribute by 3 points.
cast_spell() - accepts another Character instance as a parameter and subtracts attack/life to the other character’s life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).'''

'''Once all your classes are created start testing them, create one of each character and use each of their method.'''

class Character():
    def __init__(self,name,life=20,attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def __str__(self):
        return f"\n:::: {self.name} stats :::: \n\t** life: {self.life}**\n\t** attack: {self.attack}**"
    
    def basic_attack(self,another):
        another.life -= 1

class Druid(Character):
    def __init__(self,name,life=20,attack=10):
        Character.__init__(self,name,life,attack)

    def meditate(self):
        self.life += 10
        self.attack -= 2
        # return f"{self.name} life become: {self.life} and his attack become {self.attack}"

    def animal_help(self):
        self.attack -= 5

    def fight(self,another):
        another.life -= (0.75*self.life + 0.75*self.attack)

class Warrior(Character):
    def __init__(self,name,life=20,attack=10):
        Character.__init__(self,name,life,attack)

    def brawl(self,another):
        another.life -= 2*self.attack
        self.life += 0.5*self.attack
        # return f"{another.name} life is now: {another.life}\n {self.name} life is now: {self.life}"

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self,another):
        another.attack -= 3

class Mage(Character):
    def __init__(self,name,life=20,attack=10):
        Character.__init__(self,name,life,attack)

    def curse(self,another):
        another.attack -= 2

    def summon(self):
        self.attack +=3
    
    def cast_spell(self,another):
        another.life -= self.attack/self.life


druidi = Druid(name ='druid',life=100)
warri = Warrior(name ='warrior',life=90,attack=25)
magi = Mage(name ='mage',life=110,attack=15)

print(warri)
print(druidi)
print("\n::::::::::\tWarrior VS Druidi\t:::::::::::::")
warri.brawl(druidi)
druidi.fight(warri)
print(warri)
print(druidi)
print("\n::::::::::\tWarrior train\t:::::::::::::")
warri.train()
print(warri)
