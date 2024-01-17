# File name:    Exercise1_4.py
# Author:       Eerik Vainio
# Description:  Asks user to input numbers. User can exit the program by
#               entering 0. Once the user exits the program, print
#               out the number of negative numbers.

negative_numbers = 0

# Check if the input is numeric, or if it has a dash as the first
# character, check if the rest of the characters are numbers.
def check_valid_input(input):
    if(input.isnumeric() or (input[0] == "-" and input[1:].isnumeric())):
        return True
    
# When the length of characters in the input is greater than 1,
# check if the first character is a dash, and the rest are numbers.
def check_negative(input):
    if(len(input) > 1 and input[0] == "-"):
        return True

# Call check_valid_input to determine correct input,
# if it returns true, check if the input is 0, in which case
# break the loop. Finally call check_negative function to
# determine whether the number is negative.
while(True):
    user_input = input("Enter an integer: ")

    if(not check_valid_input(user_input)):
        print(f'"{user_input}" is not a valid number')
    else:
        if(user_input == "0"):
            break

# Check for negative numbers
        if(check_negative(user_input)):
            negative_numbers += 1

print(f'Negative numbers: {negative_numbers}')