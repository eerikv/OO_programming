# File name:    Exercise6.py
# Author:       Eerik Vainio
# Student ID:   2204661
# Description:  A simulation of a mammal and the interactions between
#               it and other objects.

import random
import os
import time

class Mammal:
    def __init__(self, name):
        self.hunger = self.thirst = self.energy = 100
        self.speed = random.randint(1,99)
        self.name = name
        self.habitat = "Savannah"
        
        print(f'{self.name} was born with the speed: {self.speed}')

    def __str__(self):
        return f'{self.name} currently living in {self.habitat}'

    def taxResources(self):
        self.hunger -= 5
        self.thirst -= 5
        self.energy -= 5

    def Hunt(self, prey):
        self.taxResources()
        if self.speed > prey.speed:
            self.hunger += prey.weight
            if self.hunger > 100:
                self.hunger = 100
            return f'Hunt successful, {self.name} ate {prey.weight}kg of meat and its hunger is now {self.hunger}/100'
        else:
            return f'The {prey.name} is {prey.speed - self.speed} units faster than the {self.name}, and gets away'
        
    def MoveToHabitat(self, habitat):
        self.taxResources()
        if habitat.name == self.habitat:
            return f'{self.name} already lives in {habitat}'
        else:
            self.habitat = habitat.name
            return f'{self.name} moves to {habitat}'
        
    def Sleep(self, shelter):
        self.taxResources()
        self.energy = 100
        return f'{self.name} goes to sleep {shelter.relativeLocation} a {shelter.name} and is now full of energy'

        
    def RunAround(self):
        self.taxResources()
        if self.speed < 100:
            self.speed += 5
            if self.speed > 100:
                self.speed = 100
            return f'{self.name} runs around the {self.habitat} and is now faster with the speed of {self.speed}'
        else:
            return f'{self.name} is already as fast as it can be'
        
    def Drink(self, waterSource):
        self.taxResources()
        self.thirst += 20
        if self.thirst > 100:
            self.thirst = 100
        return f'{self.name} drinks from a {waterSource} and its thirst is now {self.thirst}/100'
        
class Prey:
    def __init__(self, name):
        self.speed = random.randint(1,99)
        self.weight = random.randint(1,50)
        self.name = name

    def __str__(self):
        return self.name
    
class Habitat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
class Shelter:
    def __init__(self, name, relativeLocation):
        self.name = name
        self.relativeLocation = relativeLocation

    def __str__(self):
        return f'A shelter {self.relativeLocation} a {self.name.lower()}'
    
class WaterSource:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} full of water'


# Initialize variables and object instances

habitatList = preyList = shelterList = [0,0,0]

zebra = Prey("Zebra")
elephant = Prey("Elephant")
jackal = Prey("Jackal")

savannah = Habitat("Savannah")
desert = Habitat("Desert")
forest = Habitat("Forest")

cave = Shelter("Cave", "in")
palmTree = Shelter("Palm tree", "under")
abandonedCottage = Shelter("Abandoned cottage", "in")

lake = WaterSource("Lake")
river = WaterSource("River")
puddle = WaterSource("Puddle")

habitatList = [savannah, desert, forest]
preyList = [zebra, elephant, jackal]
shelterList = [cave, palmTree, abandonedCottage]
waterSourceList = [lake, river, puddle]

# Game

os.system('cls')

while True:
    userInput = input("Create a mammal: ")
    if userInput.isalpha():
        mammal = Mammal(userInput)
        break
    else:
        print(f'"{userInput}" is not a valid name for a mammal')

while True:
    os.system('cls')
    print(f'{mammal.name}:\nEnergy: {mammal.energy}, Hunger: {mammal.hunger}, Thirst: {mammal.thirst}\nSpeed: {mammal.speed}, Habitat: {mammal.habitat}\n')
    print("0: quit\n1: Hunt\n2: Move to a habitat\n3: Sleep in a shelter\n4: Run around in the habitat\n5: Drink from a water source")
    
    while True:
        userInput = input("Command: ")
        if userInput.isnumeric():
            userInput = int(userInput)
            break
        print(f'"{userInput}" is not a valid command')
        
    
    match userInput:
        case 0:
            print("Quitting the simulation")
            break
        case 1:
            os.system('cls')
            print("Select a prey to hunt:")
            for i in range(len(preyList)):
                print(f'{i}: {preyList[i]}')
            while True:
                huntInput = input("Command: ")
                if huntInput.isnumeric():
                    if int(huntInput) <= len(preyList):
                        break
                print(f'"{huntInput}" is not a valid command')

            print(mammal.Hunt(preyList[int(huntInput)]))
            time.sleep(3)
        case 2:
            os.system('cls')
            print("Select a habitat to move to: ")
            for i in range(len(habitatList)):
                print(f'{i}: {habitatList[i]}')
            while True:
                habitatInput = input("Command: ")
                if habitatInput.isnumeric():
                    if int(habitatInput) <= len(habitatList):
                        break
                print(f'"{habitatInput}" is not a valid command')

            print(mammal.MoveToHabitat(habitatList[int(habitatInput)]))
            time.sleep(3)
        case 3:
            randomShelter = shelterList[random.randint(0, len(shelterList)-1)]
            print(mammal.Sleep(randomShelter))
            time.sleep(3)
        case 4:
            print(mammal.RunAround())
            time.sleep(3)
        case 5:
            randomWaterSource = waterSourceList[random.randint(0, len(waterSourceList)-1)]
            print(mammal.Drink(randomWaterSource))
            time.sleep(3)
        case _:
            print(f'"{userInput}" is not a valid command')
            time.sleep(3)