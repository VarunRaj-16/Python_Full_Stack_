print("\n" + "=" * 60)
print("11. TUPLE OPERATIONS")
print("=" * 60)

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print("Concatenation:", t1 + t2)
# Repetition
print("Repetition:", (1, 2) * 3)
# Indexing
data_t = (10, 20, 30, 40)
print("First element:", data_t[0])
print("Last element:", data_t[-1])
# Slicing
print("Slicing [1:4]:", data_t[1:4])
print("Reverse:", data_t[::-1])
# Membership
print("20 in data_t:", 20 in data_t)
print("100 not in data_t:", 100 not in data_t)


print("\n" + "=" * 60)
print("12. BUILT-IN TUPLE FUNCTIONS")
print("=" * 60)

tuple_nums = (10, 20, 5, 30)
print("len():", len(tuple_nums))
print("max():", max(tuple_nums))
print("min():", min(tuple_nums))
print("sum():", sum(tuple_nums))
print("sorted():", sorted(tuple_nums))
print("tuple('abc'):", tuple("abc"))
print("any((0,0,1)):", any((0, 0, 1)))
print("all((1,2,3)):", all((1, 2, 3)))


