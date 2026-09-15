# COMPLETE LISTS & TUPLES DEMONSTRATION
print("=" * 60)
print("1. INTRODUCTION TO LISTS")
print("=" * 60)

# Creating lists using [] and list()
numbers = [10, 20, 30]
names = ["Ravi", "Teja", "Ankit"]
mixed = [10, "Python", 5.5, True]
empty_list = list()
print("numbers:", numbers)
print("names:", names)
print("mixed:", mixed)
print("empty_list:", empty_list)

print("\n" + "=" * 60)
print("2. LIST OPERATIONS")
print("=" * 60)

# Concatenation (+) → Joining two lists
list_a = [1, 2]
list_b = [3, 4]
print("Concatenation:", list_a + list_b)

# Repetition (*) → Repeating list elements
print("Repetition:", [1, 2] * 3)

# Indexing → Accessing elements using index
data_list = [10, 20, 30, 40]
print("First element:", data_list[0])
print("Last element:", data_list[-1])

# Slicing → Extracting part of a list
print("Slicing [1:4]:", data_list[1:4])
print("Reverse list:", data_list[::-1])

