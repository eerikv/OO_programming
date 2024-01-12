# File name: Exercise1_4.py
# Author: Eerik Vainio
# Description:  Asks user to input numbers. User can exit the program by
#               entering 0. Once the user exits the program, print
#               out the number of negative numbers.

number_list = []

def check_valid_input(input):
    if(input.isnumeric() or (input[0] == "-" and input[1:].isnumeric())):
        return True
    
def check_negative(input):
    if(len(input) > 1 and input[0] == "-"):
        return True

while(True):
    user_input = input("Enter an integer: ")

    if(not check_valid_input(user_input)):
        print(f'"{user_input}" is not a valid number')
    else:
        if(user_input == "0"):
            break

        if(check_negative(user_input)):
            number_list.append(user_input)

print(f'Negative inputs: {len(number_list)}')