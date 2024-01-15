# File name:    Exercise1_10.py
# Author:       Eerik Vainio
# Description:  A phone book application where user can either add
#               new entries, or query for existing name-number combinations.

phonebook = {}

# Check if every character in the string is either alphabetic or space.
def check_name(name):
    for x in name:
        if(not x.isalpha() and not x.isspace()):
            return False
    return True

# Check if every character in the string is either numeric or a dash.
def check_number(number):
    for x in number:
        if(not x.isnumeric() and not x == "-"):
            return False
    return True


# Main loop
while(True):

    # Ask for user command. Break only on correct input.
    while(True):
        user_input = input("command (1 search, 2 add, 3 quit): ")
        if(user_input in ("1", "2", "3")):
            break
        else:
            print(f'"{user_input}" is not a valid input.')

    # Check if the user wants to exit the program.
    if(int(user_input) == 3):
        break

    # Inputs 1 and 2
    match int(user_input):
        # Search input. Ask for a name and output the correct number
        case 1:
            input_query = input("name: ")
            if(input_query in phonebook):
                print(phonebook[input_query])
            else:
                print(f'{input_query} is not in the phonebook.')
        # Add input. Ask for name and number, break loops only on correct inputs.
        # Finally add the name-number combination to the phonebook dictionary.
        case 2:
            while(True):
                input_name = input("name: ")
                if(check_name(input_name)):
                    break
                else:
                    print(f'"{input_name}" is not a valid name.')

            while(True):
                input_number = input("number: ")
                if(input_number.isnumeric()):
                    break
                elif(len(input_number) == 0):
                    print("no number")
                else:
                    print(f'"{input_number}" is not a valid number.')
            
            phonebook[input_name] = input_number
