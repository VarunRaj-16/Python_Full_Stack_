print("3. ATM ABSTRACTION - DIFFERENT BANKS")
from abc import ABC, abstractmethod
class BankATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class SBI(BankATM):
    def __init__(self):
        self.balance = 10000
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"SBI: ₹{amount} withdrawn.")
        else:
            print("SBI: Insufficient funds.")
    def deposit(self, amount):
        self.balance += amount
        print(f"SBI: ₹{amount} deposited.")
    def check_balance(self):
        print(f"SBI: Balance is ₹{self.balance}")
class ICICI(BankATM):
    def __init__(self):
        self.balance = 15000
        self.fee = 10
    def withdraw(self, amount):
        total = amount + self.fee
        if total <= self.balance:
            self.balance -= total
            print(f"ICICI: ₹{amount} withdrawn with ₹{self.fee} fee.")
        else:
            print("ICICI: Insufficient funds.")
    def deposit(self, amount):
        self.balance += amount
        print(f"ICICI: ₹{amount} deposited.")
    def check_balance(self):
        print(f"ICICI: Balance is ₹{self.balance}")
sbi = SBI()
sbi.withdraw(2000)
sbi.check_balance()
icici = ICICI()
icici.withdraw(1000)
icici.check_balance()

