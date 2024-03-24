# File name:    Exercise5.py
# Author:       Eerik Vainio
# Student ID:   2204661
# Description:  A simulation of different mammals and the interactions between them.

import random

class Mammal:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.hunger = self.thirst = self.energy = 100

    def __str__(self):
        return f'{self.name} the {self.species}'

    def Hunt(self, otherMammal):
        if (self.hierarchy > otherMammal.hierarchy):
            print(f'{self} succesfully hunted {otherMammal}.')
            self.Eat()
        else:
            print(f'{self.name} failed to hunt {otherMammal.name}, since {self.species}s are much weaker than {otherMammal.species}s.')

    def Eat(self):
        self.hunger += 20
    
    def Drink(self):
        self.thirst += 20

    def Sleep(self):
        self.energy = 100

    def PlayWith(self, otherMammal):
        if (self.hierarchy == otherMammal.hierarchy):
            print(f'{self} and {otherMammal} played together.')
        else:
            print(f'{self} and {otherMammal} are unable to play together.')

class Mouse(Mammal):
    def __init__(self, name: str, age: int, gender: str, senseOfSmell: int):
        super().__init__(name, age, gender)
        self.species = "mouse"
        self.senseOfSmell = senseOfSmell
        self.hierarchy = 0
    
    def TrackCheese(self):
        if (random.randInt(1, 100) + self.senseOfSmell >= 50):
            print(f'{self} successfully found some cheese.')
            self.Eat()
        else:
            print(f'{self} was unable to find cheese.')


class Cat(Mammal):
    def __init__(self, name: str, age: int, gender: str, furCleanliness: int):
        super().__init__(name, age, gender)
        self.species = "cat"
        self.furCleanliness = furCleanliness
        self.hierarchy = 1
    
    def LickFur(self):
        self.oldFurCleanliness = self.furCleanliness
        self.furCleanliness += 10
        print(f'{self} cleaned themselves, and their fur cleanliness increased from {self.oldFurCleanliness} to {self.furCleanliness}.')

class Dog(Mammal):
    def __init__(self, name: str, age: int, gender: str, barkingLoudness: int):
        super().__init__(name, age, gender)
        self.species = "dog"
        self.barkingLoudness = barkingLoudness
        self.hierarchy = 2
    
    def PracticeBarking(self):
        self.barkingLoudness += 10
        print(f'{self} practiced barking, and they can now bark at {self.barkingLoudness}dB.')

class Hyena(Mammal):
    def __init__(self, name: str, age: int, gender: str, teethSharpness: int):
        super().__init__(name, age, gender)
        self.species = "hyena"
        self.teethSharpness = teethSharpness
        self.hierarchy = 3
    
    def SharpenTeeth(self):
        self.teethSharpness += 10
        print(f'{self} sharpened their teeth.')

class Lion(Mammal):
    def __init__(self, name: str, age: int, gender: str, maneSize: int):
        super().__init__(name, age, gender)
        self.species = "lion"
        self.maneSize = maneSize
        self.hierarchy = 4