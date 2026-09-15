# DAY 27 - ENCAPSULATION & ABSTRACTION
from abc import ABC, abstractmethod
print("1. ENCAPSULATION - BANK ACCOUNT")
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def show_balance(self):
        print(f"{self.name}, your balance is ₹{self.__balance}")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
acc = BankAccount("Varun", 5000)
acc.show_balance()
acc.deposit(2000)
acc.withdraw(1000)
acc.show_balance()