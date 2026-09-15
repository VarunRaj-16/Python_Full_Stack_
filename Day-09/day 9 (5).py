print("14. TUPLE PACKING & UNPACKING\n")

# Packing → Multiple values automatically stored in a tuple
packed = 10, 20, 30
print("Packed tuple:", packed)
# Unpacking → Extracting tuple elements into variables
a, b, c = packed
print("Unpacked values:", a, b, c)

print("\n15. NESTED TUPLES\n")

nested_tuple = ((1, 2), (3, 4), (5, 6))
print("nested_tuple[0]:", nested_tuple[0])
print("nested_tuple[1][1]:", nested_tuple[1][1])


print("\n16. IMMUTABILITY & MUTABLE OBJECTS INSIDE TUPLE\n")

'''Trying to modify tuple element will raise TypeError data = (10, 20, 30), data[0] = 100, TypeError, But mutable objects inside tuple can be modified'''

mutable_inside = (10, [20, 30], 40)
mutable_inside[1].append(50)
print("After modifying list inside tuple:", mutable_inside)

