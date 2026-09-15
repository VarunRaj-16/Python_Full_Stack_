#1. String Input
name = input("Enter your full name: ")
print(name)

#2. Integer Input
quantity = int(input("Enter the number of items: "))
print(quantity)

#3. Float Input
price = float(input("Enter the product price: "))
print(price)

#4. Input as List (Space-separated)
names = input("Enter employee names (space-separated): ").split()
print(names)

#5. Input as List (Comma-separated)
tags = input("Enter tags (comma-separated): ").split(',')
print(tags)

#6. List of Integers
marks = list(map(int, input("Enter marks: ").split()))
print(marks)

#7. List of Floats
weights = list(map(float, input("Enter weights: ").split()))
print(weights)

#8. Tuple Input
dimensions = tuple(map(int, input("Enter length, width, height: ").split()))
print(dimensions)

#9. Set Input
selected_ids = set(map(int, input("Enter selected image IDs: ").split()))
print(selected_ids)

#10. Dictionary Input using eval()
profile = eval(input("Enter user profile as a dictionary: "))
print(profile)

#11. Multiple Inputs with Unpacking
username, password = input("Enter username and password: ").split()
print("Username:", username)
print("Password:", password)
