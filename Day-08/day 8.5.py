print("\n" + "=" * 60)
print("13. TUPLE METHODS")
print("=" * 60)
# Tuples have only two methods because they are immutable
sample_tuple = (1, 2, 2, 3, 2)
# count() → Counts occurrences of an element
print("count(2):", sample_tuple.count(2))
# index() → Returns first occurrence index
print("index(3):", sample_tuple.index(3))
print("\n" + "=" * 60)
print("14. TUPLE PACKING & UNPACKING")
print("=" * 60)
# Packing → Multiple values automatically stored in a tuple
packed = 10, 20, 30
print("Packed tuple:", packed)
# Unpacking → Extracting tuple elements into variables
a, b, c = packed
print("Unpacked values:", a, b, c)
print("\n" + "=" * 60)
print("15. NESTED TUPLES")
print("=" * 60)
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("nested_tuple[0]:", nested_tuple[0])
print("nested_tuple[1][1]:", nested_tuple[1][1])
print("\n" + "=" * 60)
print("16. IMMUTABILITY & MUTABLE OBJECTS INSIDE TUPLE")
print("=" * 60)
# Trying to modify tuple element will raise TypeError
# data = (10, 20, 30)
# data[0] = 100   # TypeError
# But mutable objects inside tuple can be modified
mutable_inside = (10, [20, 30], 40)
mutable_inside[1].append(50)
print("After modifying list inside tuple:", mutable_inside)
print("\n" + "=" * 60)
print("END OF LISTS & TUPLES DEMONSTRATION")
print("=" * 60)


