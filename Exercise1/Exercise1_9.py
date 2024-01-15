# File name:    Exercise1_9.py
# Author:       Eerik Vainio
# Description:  A program that prints a random number between 1-6.

import random

# Return a random number between 1-6
def random_number_generator():
    return random.randint(1,6)

print(random_number_generator())