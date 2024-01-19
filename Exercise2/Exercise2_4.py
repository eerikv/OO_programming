# File name:    Exercise2_4.py
# Author:       Eerik Vainio
# Description:  A set of functions, which return factorials of numbers
#               1 to n in a dictionary.

def factorials(n: int):
    factorial_dictionary = {}

    for i in range(n):
        factorial_dictionary[n] = calculate_factorial(n)
        n -= 1
    
    return factorial_dictionary

def calculate_factorial(n: int):
    total = 1

    for i in range(n):
        total = total * n
        n -= 1

    return total

k = factorials(10)
print(k[1])
print(k[3])
print(k[5])
print(k[10])
