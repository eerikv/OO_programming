# File name:    Exercise8_EerikVainio.py
# Author:       Eerik Vainio
# Student ID:   2204661
# Description:  A simulation of a mammal and the interactions between
#               it and other objects.

import os
import random

class Mammal:
    def __init__(self, name):
        self.name = name
        self.hunger = self.thirst = self.energy = 100
        
    def __str__(self):
        return f'{self.name} the mammal'
    
    def taxResources(self):
        self.hunger -= 5
        self.thirst -= 5
        self.energy -= 5
    
    def Hunt(self):
        self.taxResources()
        if(preyAmount > 0):
            if(self.hunger <= 95):
                self.hunger += 20
                return f'{self.name} hunts down prey and eats it'
            else:
                return f'But {self.name} is too full to chase down prey'
        else:
            return f'But {self.name} cannot find prey nearby'

    def Drink(self):
        self.taxResources()
        if(self.thirst <= 95):
            self.thirst += 20
            return f'{self.name} drinks some water'
        else:
            return f'But {self.name} does not need to drink right now'

    def Rest(self):
        self.taxResources()
        if(self.energy <= 95):
            self.energy += 50
            return f'{self.name} takes a nap'
        else:
            return f'But {self.name} does not feel tired right now'
    

preyAmount = 0

# Game

os.system('cls')

while True:
    userInput = input("Name the mammal: ")
    if userInput.isalpha():
        mammal = Mammal(userInput)
        break
    else:
        print(f'"{userInput}" is not a valid name for a mammal')

while True:
    os.system('cls')

    match(random.randint(1,3)):
        case(1):
            preyAmount += 1
            print("A new prey arrives closeby\n")
        case(2):
            print("The amount of prey nearby stays the same\n")
        case(3):
            if(preyAmount > 0):
                preyAmount -= 1
                print("One of the nearby prey moves away\n")
            else:
                print("The amount of prey nearby stays the same\n")

    print(f'{mammal}\nHunger: {mammal.hunger}, Thirst: {mammal.thirst}, Energy: {mammal.energy}')
    print(f'Prey currently nearby: {preyAmount}\n')
    print("0: quit\n1: Hunt prey\n2: Drink at an oasis\n3: Sleep in a cave")

    while True:
        userInput = input("Command: ")
        if userInput.isnumeric():
            userInput = int(userInput)
            break
        print(f'"{userInput}" is not a valid command')

    match userInput:
        case 0:
            print("Quitting the simulation")
        case 1:
            os.system('cls')
            print(f'{mammal.name} decides to hunt down some pray...')
            print(mammal.Hunt())
            input("\nPress enter to continue... ")
        case 2:
            os.system('cls')
            print(f'{mammal.name} decides to go drink at an oasis...')
            print(mammal.Drink())
            input("\nPress enter to continue... ")
        case 3:
            os.system('cls')
            print(f'{mammal.name} goes into a cave to get some rest...')
            print(mammal.Rest())
            input("\nPress enter to continue... ")



