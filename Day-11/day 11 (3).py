print("5. Stock Availability Example")
stock = int(input("Enter stock quantity: "))
if stock > 20:
    print("Full stock available")
elif stock > 0:
    print("Limited stock available")
else:
    print("Out of stock")
print("6. NESTED if")
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
if age >= 18:
    if weight >= 50:
        print("Eligible")
    else:
        print("Not eligible due to weight")
else:
    print("Not eligible due to age")
print("End")


