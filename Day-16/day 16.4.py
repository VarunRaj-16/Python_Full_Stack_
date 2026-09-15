print("7. SET METHODS – COPY & RELATION")
a = {1, 2, 3}
b = {2, 3, 4}
print("copy():", a.copy())
print("union():", a.union(b))
print("intersection():", a.intersection(b))
print("difference():", a.difference(b))
print("symmetric_difference():", a.symmetric_difference(b))
print("issubset():", {1, 2}.issubset(a))
print("issuperset():", a.issuperset({1, 2}))
print("isdisjoint():", a.isdisjoint({7, 8}))
print("8. FROZENSET")
data = frozenset({10, 20, 30})
print("frozenset:", data) # data.add(40)                    # Error – frozenset is immutable
