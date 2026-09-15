# del → Deletes element or entire list
data = [100, 200, 300]
del data[0]
print("After del data[0]:", data)
print("\n" + "=" * 60)
print("6. LIST METHODS - SEARCH")
print("=" * 60)

search_list = [10, 20, 30, 20, 40]
# index() → Returns the index of first occurrence
print("index(20):", search_list.index(20))
# count() → Counts how many times an element appears
print("count(20):", search_list.count(20))


print("\n" + "=" * 60)
print("7. LIST METHODS - SORTING & REVERSING")
print("=" * 60)

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


