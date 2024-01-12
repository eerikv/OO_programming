numberList = []
stringList = []

def fill_list(list, numeric):
    while(len(list) < 10):
        if (numeric == 1):
            userInput = input(f'Enter a number ({len(list)}/10): ')
            if(userInput.isnumeric()):
                list.append(userInput)
            else:
                print(f'{userInput} is not a valid number.')
        else:
            userInput = input(f'Enter a string ({len(list)}/10): ')
            list.append(userInput)

fill_list(numberList, 1)
fill_list(stringList, 0)




#while(len(numberList) < 10):
#    userInput = input("Enter a number: ")
#    if(userInput.isnumeric()):
#        numberList.append(userInput)
#    else:
#        print(f'{userInput} is not a valid number.')

print(numberList)
print(stringList)