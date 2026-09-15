print("\n" + "=" * 60)
print("8. LIST METHODS - COPYING")
print("=" * 60)

original_list = [1, 2, 3]
copied_list = original_list.copy()
print("Original:", original_list)
print("Copied:", copied_list)


print("\n" + "=" * 60)
print("9. NESTED LISTS")
print("=" * 60)

nested = [[1, 2], [3, 4], [5, 6]]
print("nested[0]:", nested[0])
print("nested[1][1]:", nested[1][1])


print("\n" + "=" * 60)
print("10. INTRODUCTION TO TUPLES")
print("=" * 60)

# Creating tuples
numbers_t = (10, 20, 30)
names_t = ("Ravi", "Teja", "Ankit")
mixed_t = (10, "Python", 5.5, True)
empty_tuple = ()
single_element = (10,)          # Note the comma

print("numbers_t:", numbers_t)
print("single_element:", single_element)
print("type of (10):", type((10)))   # This is int, not tuple


