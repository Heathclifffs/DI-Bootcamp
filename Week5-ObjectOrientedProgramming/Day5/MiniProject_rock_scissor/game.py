# Mini-Project: Rock, Paper, Scissors
# Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia

# We will create a game for the user to play Rock-paper-scissors against the computer.

# The user will input his/her move (rock/paper/scissors),
# and the computer will select either rock, paper or scissors at random.
# We will then compare the user’s move with the computer’s move, and determine the results of the game:

# The user won

# The computer won (the user lost)
# A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

# The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.

# Here’s some example output:

# Mini Project2




# Instructions
# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.


# Steps
# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.


import random

class Game():
    def get_user_item(self):
        selection = True
        while selection :
            user = input("Select (R)ock (P)aper or (C)isor:  ").lower()
            if  user == "r" or user == "c" or user == "p":
                selection = False
        return user

    def get_computer_item(self):
        return random.choice(['r','p','c'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif user_item == 'r' and computer_item == 'p':
            return 'loss'
        elif user_item == 'p' and computer_item == 'c':
            return 'loss'
        return 'win'
    @staticmethod
    def play():
        user = Game().get_user_item()
        computer = Game().get_computer_item()
        result = Game().get_game_result(user,computer)
        if result == 'draw':
            decision = 'You drew'
        elif result == 'loss':
            decision = 'You lose'
        else:
            decision = 'You won'
        print(f"You selected {user}. The computer selected {computer}. "+decision)
        return result

