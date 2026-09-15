print("7. LIST METHODS - SORTING & REVERSING \n")

scores = [40, 10, 30, 20]
# sort() → Sorts the original list
scores.sort()
print("After sort():", scores)
# reverse() → Reverses the list
scores.reverse()
print("After reverse():", scores)
# sorted() → Returns a new sorted list (original remains unchanged)
original = [5, 1, 4, 2]
print("sorted():", sorted(original))
print("Original list:", original)

print("8. LIST METHODS - COPYING \n")

original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Original:", original_list)
print("Copied:", copied_list)

print("9. NESTED LISTS")

nested = [[1, 2], [3, 4], [5, 6]]
print("nested[0]:", nested[0])
print("nested[1][1]:", nested[1][1])

print("10. INTRODUCTION TO TUPLES \n")

# Creating tuples
numbers_t = (10, 20, 30)
names_t = ("Ravi", "Teja", "Ankit")
mixed_t = (10, "Python", 5.5, True)
empty_tuple = ()
single_element = (10,)          # Note the comma
print("numbers_t:", numbers_t)
print("single_element:", single_element)
print("type of (10):", type((10)))   # This is int, not tuple


