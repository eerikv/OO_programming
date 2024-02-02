# File name:    Exercise3_5.py
# Author:       Eerik Vainio
# Description:  A credit card program. User can deposit or subtract
#               funds from their card, and use a payment terminal to
#               buy different lunches.

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if(self.balance > amount):
            self.balance -= amount
            return(True)
        else:
            return(False)
        pass
        # The amount should be subtracted from the balance only if
        # there is enough money on the card.
        # If the payment is successful, the method returns True. 
        # Otherwise it returns False.
    

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        # A ordinary lunch costs 2.95 euros.
        # Increase the value of the funds at the terminal by the 
        # price of the lunch, increase the number of lunches sold, 
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        if(payment >= 2.95):
            self.funds += 2.95
            self.funds = float(format(self.funds, ".2f"))
            self.ordinaries += 1
            return(payment - 2.95)
        else:
            return(2.95)

    def eat_luxury(self, payment: float):
        # A sluxury lunch costs 5.90 euros.
        # Increase the value of the funds at the terminal by the 
        # price of the lunch, increase the number of lunches sold, 
        # and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover
        # the price, the lunch is not sold, and the entire sum is returned.
        if(payment >= 5.90):
            self.funds += 5.90
            self.funds = float(format(self.funds, ".2f"))
            self.luxuries += 1
            return(payment - 5.90)
        else:
            return(5.90)

    def eat_ordinary_lunchcard(self, card: LunchCard):
        # A ordinary lunch costs 2.95 euros.
        # If there is enough money on the card, 
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if(card.balance >= 2.95):
            card.balance -= 2.95
            card.balance = float(format(card.balance, ".2f"))
            self.funds += 2.95
            self.funds = float(format(self.funds, ".2f"))
            self.ordinaries += 1
            return(True)
        else:
            return(False)


    def eat_luxury_lunchcard(self, card: LunchCard):
        # A luxury lunch costs 5.90 euros.
        # If there is enough money on the card, 
        # subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if(card.balance >= 5.90):
            card.balance -= 5.90
            card.balance = float(format(card.balance, ".2f"))
            self.funds += 5.90
            self.funds = float(format(self.funds, ".2f"))
            self.luxuries += 1
            return(True)
        else:
            return(False)
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        card.balance = float(format(card.balance, ".2f"))
        pass

#You may use the following code to test your function:

if __name__ == "__main__":
    
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.ordinaries)
    print("Special lunches sold:", exactum.luxuries)