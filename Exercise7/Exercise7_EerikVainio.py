# File name:    Exercise7.py
# Author:       Eerik Vainio
# Student ID:   2204661
# Description:  A simulation of a mammal and the interactions between
#               it and other objects.

import random
import time

class Mammal():
    def __init__(self):
        self.state = "resting"

    def Hunt(self):
        if (random.randint(1, 2) == 1):
            print(f'The mammal found a target and starts to hunt it')
            self.state = "hunting"
            self.Hunting()
        else:
            print(f'The mammal did not find a target to hunt.')

    def Hunting(self):
        self.distanceToPrey = 20
        self.speed = 5
        while (self.distanceToPrey > 0):
            self.speed += random.randint(-5, 5)
            self.distanceToPrey -= self.speed
            if (self.speed > 0):
                print(f'The mammal is closing in on the prey.')
            elif (self.speed < 0):
                print(f'The mammal is losing ground to the prey.')
            else:
                print("The mammal is keeping up with the prey.")
            print(f'The distance between the animals is: {self.distanceToPrey}.')

mammal1 = Mammal()
mammal1.Hunt()