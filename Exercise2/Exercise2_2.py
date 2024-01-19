# File name:    Exercise2_2.py
# Author:       Eerik Vainio
# Description:  Coin object and tossing

import random

# Class definition
class Coin:
    def __init__(self):
        self.sideup = "Heads"
    
    def toss_the_coin(self):
        match random.randint(0,4):
            case 0:
                self.sideup = "Heads"
            case 1:
                self.sideup = "Tails"
            case 2:
                self.sideup = "Coin lands on its side"
            case 3:
                self.sideup = "Coin drops on the ground and disappears in a rabbit hole"
            case 4:
                self.sideup = "Coin defies gravity and gets lost on a wormhole in space"
    
    def get_sideup(self):
        return self.sideup
    
# Main function definition  
def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

# Calling the main function
main()