print("5. REAL-WORLD EXAMPLE - SHOP BILL")
class Shop:
    def calculate_bill(self, item1, item2=0):
        total = item1 + item2
        print(f"Total Bill (No Discount): ₹{total}")
class SpecialCustomer(Shop):
    def calculate_bill(self, item1, item2=0):
        total = item1 + item2
        discount = total * 0.1
        final_amount = total - discount
        print(f"Total Bill after 10% discount: ₹{final_amount}")
print("Normal Customer:")
s1 = Shop()
s1.calculate_bill(100)
s1.calculate_bill(100, 200)
print("Special Customer:")
s2 = SpecialCustomer()
s2.calculate_bill(100)
s2.calculate_bill(100, 200)
