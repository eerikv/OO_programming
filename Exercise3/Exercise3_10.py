# File name:    Exercise3_10.py
# Author:       Eerik Vainio
# Description:  A bank account class, which has functionality for
#               depositing and withdrawing money. User can also check
#               the balance of the account. For every transaction, 1% of
#               the balance is subtracted.

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        self._service_charge()
    
    def withdraw(self, amount: float):
        self.balance -= amount
        self._service_charge()

    def balance(self):
        return self.balance
    
    def _service_charge(self):
        self.balance -= (self.balance / 100)

account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
