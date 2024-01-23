# File name:    Exercise3_3.py
# Author:       Eerik Vainio
# Description:  A lunchcard class which has functionality for depositing money,
#               and buying different priced meals.

import math

class LunchCard():
    def __init__(self, balance: float):
        self.balance = float(format(balance, ".2f"))

    def __str__(self):
        return(f'The balance is {round(self.balance, 2)} euros.')

    def eat_ordinary(self):
        if(self.balance > 2.95):
            self.balance -= 2.95
        else:
            print(f'Insufficient funds. Current balance: {round(self.balance, 2)} euros.')
    
    def eat_luxury(self):
        if(self.balance > 5.90):
            self.balance -= 5.90
        else:
            print(f'Insufficient funds. Current balance: {round(self.balance, 2)} euros.')

    def deposit_money(self, deposit: float):
        if(deposit > 0):
            self.balance += deposit
        else:
            raise ValueError("The deposit value cannot be negative: " + str(deposit))

card = LunchCard(50)
print(card)

card.eat_ordinary()
print(card)

card.eat_luxury()
card.eat_ordinary()
print(card)

print("Creating new card..")

card2 = LunchCard(10)
print(card2)
card2.deposit_money(15)
print(card2)
card2.deposit_money(10)
print(card2)
card2.deposit_money(200)
print(card2)
card2.deposit_money(-10)