# File name:    Exercise1_7.py
# Author:       Eerik Vainio
# Description:  Generates values with arithmetic progression until reaching
#               a user defined max value. Finally prints out the number of
#               the terms, the sum of the terms, and the sum of the squared
#               terms.

import math

max_value = number_of_terms = sum_of_terms = sum_of_sq_terms = 0
ap_value = 3

# Ask user for the max value, repeat if the value is invalid
while(True):
    user_input = input("Give the maximum value: ")
    if(user_input.isnumeric()):
        max_value = int(user_input)
        break
    else:
        print(f'"{user_input}" is not a valid value.')

# Add 3 to the ap value on each loop, break when the ap value
# is greater than the max value.
while(True):
    if(ap_value > max_value):
        break
    else:
        number_of_terms += 1
        sum_of_terms += ap_value
        sum_of_sq_terms += math.sqrt(ap_value)
        ap_value += 3

print(f'Number of terms: {number_of_terms}')
print(f'Sum of terms: {sum_of_terms}')
print(f'Sum of squared terms: {sum_of_sq_terms}')



