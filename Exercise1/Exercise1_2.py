# File name: Exercise1_2.py
# Author: Eerik Vainio
# Description:  1. Asks values from user to fill a list of integers and a list
#               of strings, and prints out the lists.
#               2. Changes the values in the number list to random ones,
#               and prints out that list.

import random

# Initialize lists
number_list = []
string_list = []

# Ask for user input, and append the input to the corresponding list.
# Loop for 10 times.
def fill_list(list, numeric):
    while(len(list) < 10):
        if (numeric == 1):
            user_input = input(f'Enter a number ({len(list)}/10): ')
            # Append the input to the list if it's numeric,
            # print out a message if it is not.
            if(user_input.isnumeric()):
                list.append(int(user_input))
            else:
                print(f'"{user_input}" is not a valid number.')
        else:
            user_input = input(f'Enter a string ({len(list)}/10): ')
            # Only append the input if it's length is greater than 0.
            if(len(user_input) > 0):
                list.append(user_input)
            else:
                print('Invalid input.')

# Call fill_list for both of the lists
fill_list(number_list, 1)
fill_list(string_list, 0)

print(f'number_list: {number_list}')
print(f'string_list: {string_list}')

# Change the values in number_list to random integers between 0-999
for i in range(len(number_list)):
    number_list[i] = random.randint(0, 999)

print(f'number_list: {number_list}')