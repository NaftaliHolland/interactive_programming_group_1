#!/usr/bin/python3

class Account:
    
    def __init__(self, amount):
        self.amount = amount

    def debit(self, amount):
        """reduces the amount in tha account"""
        if self.amount > amount:
            print("Debit amount exceeds account balance");
        else:
            self.amount -= amount

    def withdraw(self):
        pass

    def account_balance(self):
        """returns the amount in the account"""
        return self.amount

my_account = Account(500)
print(my_account.account_balance())
my_account.debit(200)
print(my_account.account_balance())
my_account.debit(500)
