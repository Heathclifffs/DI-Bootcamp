# Exercise 2 : Dungeons & Dragons
# Instructions
# For a game of Dungeons & Dragons, each player starts by generating a character they can play with. This character has, among other things, six attributes/stats:
# Strength
# Dexterity
# Constitution
# Intelligence
# Wisdom
# Charisma

# These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and record the sum of the largest three dice. You do this six times, once for each ability.
# For example, the six throws of four dice may look like:
# 5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
# 3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
# 1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
# 2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
# 3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
# 6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.

# Create a class called Character and a class called Game for this exercise.

# The point of this exercise is to generate characters for players looking to start a game quickly.
# Start by asking the user how many players are playing.
# Each user then creates his/her character, let them establish what the characters name and age are.
# Output the characters created into the following formats:
# txt: a nicely formatted text file for the players to use
# json: a json file of all the characters and attributes


# Hint: the Character class should be in charge of creating characters, the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt
import random
import json

class Character():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.strength = self.rand_points()
        self.dexterity = self.rand_points()
        self.constitution = self.rand_points()
        self.intelligence = self.rand_points()
        self.wisdom =self.rand_points()
        self.charisma = self.rand_points()

    def rand_points(self):
        liste = [random.randint(1,6) for i in range(4)]
        return sum(liste) - min(liste)

    # def ability(self):
    #     self.strength = self.rand_points()
    #     self.dexterity = self.rand_points()
    #     self.constitution = self.rand_points()
    #     self.intelligence = self.rand_points()
    #     self.wisdom =self.rand_points()
    #     self.charisma = self.rand_points()

    

class Game():
    def start(self):
        all_players = {} # for json file
        all_players["players"] = []
        players = input("How many players are playing:\t_ ")
        try:
            num = int(players)
        except:
            print("Your entry not correct")
        for i in range(num):
            name = input(f"Chararcter number {i} name:\t_ ")
            age = input(f"Chararcter number {i} age:\t_ ")
            character = Character(name,age)
            file = f"C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExercisesXpNinja/{character.name}.txt"   
            with open(file,"w") as f:
                f.write(f"Name : {character.name}\n")
                f.write(f"Age : {character.age}\n")
                f.write(f"----\tStats  ----\n")
                f.write(f"Strength : {character.strength}\n")
                f.write(f"Dexterity : {character.dexterity}\n")
                f.write(f"Constitution : {character.constitution}\n")
                f.write(f"Intelligence : {character.intelligence}\n")
                f.write(f"Wisdom : {character.wisdom}\n")
                f.write(f"Charisma : {character.charisma}\n")
            dict = {
                "Name" : character.name,
                "Age" :character.age,
                "Strength" : character.strength,
                "Dexterity" : character.dexterity,
                "Constitution": character.constitution,
                "Intelligence" : character.intelligence,
                "Wisdom" : character.wisdom,
                "Charisma" : character.charisma
            }
            all_players["players"].append(dict)
        json_file = "C:/Users/SHT/Desktop/Nouveau dossier/Day4/ExercisesXpNinja/players.json"
        with open(json_file,"w") as f:
            json.dump(all_players,f,indent = 3)
        print("Game initiated with success")

game = Game()
game.start()

            
