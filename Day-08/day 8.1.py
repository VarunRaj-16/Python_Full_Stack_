data_list = [10, 20, 30, 40]
# Membership Operators
print("20 in data_list:", 20 in data_list)
print("100 not in data_list:", 100 not in data_list)
print("\n" + "=" * 60)
print("3. BUILT-IN LIST FUNCTIONS")
print("=" * 60)
nums = [10, 20, 5, 30]
print("len():", len(nums))
print("max():", max(nums))
print("min():", min(nums))
print("sum():", sum(nums))
print("sorted():", sorted(nums))
print("list('abc'):", list("abc"))
print("\n" + "=" * 60)
print("4. LIST METHODS - ADDING ELEMENTS")
print("=" * 60)
fruits = ["apple", "banana"]
# append() → Adds a single element at the end
fruits.append("mango")
print("After append:", fruits)
# extend() → Adds multiple elements
fruits.extend(["orange", "grape"])
print("After extend:", fruits)
# insert() → Inserts element at a specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)
print("\n" + "=" * 60)
print("5. LIST METHODS - REMOVING ELEMENTS")
print("=" * 60)
items = [10, 20, 30, 20, 40]
# remove() → Removes first occurrence of the value
items.remove(20)
print("After remove(20):", items)
# pop() → Removes element using index (default last)
popped = items.pop()
print("After pop():", items, "| Popped value:", popped)
# clear() → Removes all elements
temp = [1, 2, 3]
temp.clear()
print("After clear():", temp)
# del → Deletes element or entire list
data = [100, 200, 300]
del data[0]
print("After del data[0]:", data)
