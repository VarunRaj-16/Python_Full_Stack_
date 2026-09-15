# DAY 19 - LIST COMPREHENSION COMPLETE DEMONSTRATION

print("1. WHAT IS A LIST?")
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob"]
mixed = [1, "hello", True, 3.5]
print("numbers:", numbers)
print("names:", names)
print("mixed:", mixed)

print("2. BASIC LIST COMPREHENSION EXAMPLES")
squares = [x * x for x in range(6)] # a. Square numbers
print("Squares:", squares)
numbers = [1, 2, 3, 4, 5, 6]        # b. Filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)
names = ["alice", "bob", "charlie"] # c. Uppercase strings
upper_names = [name.upper() for name in names]
print("Uppercase names:", upper_names)

