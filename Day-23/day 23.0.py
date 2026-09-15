# DAY 23 - OOP: CLASSES, OBJECTS, ATTRIBUTES & METHODSprint("=" * 65)
print("1. BASIC CLASS AND OBJECT")
class Product:
    platform = "Flipkart"                 # Class Attribute
    def display_product(self):
        print("Displaying Product Details")
    def check_stock(self):
        print("Stock Available")
laptop = Product()
mobile = Product()
print("Platform:", laptop.platform)
laptop.display_product()
mobile.check_stock()

