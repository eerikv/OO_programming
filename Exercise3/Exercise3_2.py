# File name:    Exercise3_2.py
# Author:       Eerik Vainio
# Description:  A class which takes in numbers, and outputs various data
#               on them.

# Takes in numbers and returns data on them
class NumberStats():
    def __init__(self):
        self.numbers_added = 0
        self.number_list = []
        self.sum = self.even_sum = self.odd_sum = 0
    
    def add_number(self, given_number):
        self.numbers_added += 1
        self.sum += given_number
        self.number_list.append(given_number)

    def count_numbers(self):
        return(self.numbers_added)
    
    def get_sum(self):
        return(self.sum)
    
    def average(self):
        return(self.sum/self.numbers_added)
    
    def get_even_sum(self):
        for x in self.number_list:
            if(x % 2 == 0):
                self.even_sum += x
        return(self.even_sum)
    
    def get_odd_sum(self):
        for x in self.number_list:
            if(not x % 2 == 0):
                self.odd_sum += x
        return(self.odd_sum)

    

stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())

user_stats = NumberStats()
print("Please type in integer numbers:")

# Ask for numbers from the user
while(True):
    user_input = input()

    if(user_input == "-1"):
        break
    else:
        if(user_input.isnumeric()):
            user_stats.add_number(int(user_input))
        else:
            print(f'"{user_input}" is not a valid number.')

print("Sum of numbers:", user_stats.get_sum())
print("Mean of numbers:", user_stats.average())
print("Sum of even numbers:", user_stats.get_even_sum())
print("Sum of odd numbers:", user_stats.get_odd_sum())
