print("1. INTRODUCTION TO LISTS")

# Creating lists using [] and list()
numbers = [10, 20, 30]
names = ["Ravi", "Teja", "Ankit"]
mixed = [10, "Python", 5.5, True]
empty_list = list()
print("numbers:", numbers)
print("names:", names)
print("mixed:", mixed)
print("empty_list:", empty_list)

print("2. LIST OPERATIONS")

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
# Membership Operators
print("20 in data_list:", 20 in data_list)
print("100 not in data_list:", 100 not in data_list)

print("3. BUILT-IN LIST FUNCTIONS")

nums = [10, 20, 5, 30]
print("len():", len(nums))
print("max():", max(nums))
print("min():", min(nums))
print("sum():", sum(nums))
print("sorted():", sorted(nums))
print("list('abc'):", list("abc"))


