#Bank Example (Abstract + Concrete Method)
from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan_interest(self):
        pass
    def bank_services(self):          # Concrete method
        print("Common services: Net Banking, ATM, Mobile App")
class SBI(Bank):
    def loan_interest(self):
        print("SBI interest rate is 8%")
class HDFC(Bank):
    def loan_interest(self):
        print("HDFC interest rate is 10%")
bank1 = SBI()
bank2 = HDFC()
bank1.loan_interest()
bank1.bank_services()
bank2.loan_interest()
bank2.bank_services()