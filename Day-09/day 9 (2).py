print("4. LIST METHODS - ADDING ELEMENTS")

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

print("5. LIST METHODS - REMOVING ELEMENTS")

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

print("6. LIST METHODS - SEARCH")

search_list = [10, 20, 30, 20, 40]
# index() → Returns the index of first occurrence
print("index(20):", search_list.index(20))
# count() → Counts how many times an element appears
print("count(20):", search_list.count(20))


