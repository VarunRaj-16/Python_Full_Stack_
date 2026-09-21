import numpy as np
# 10. SORTING AND UNIQUE VALUES
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
# Sorting
sorted_arr = np.sort(arr)
print(sorted_arr)
# Unique elements
unique_vals = np.unique(arr)
print(unique_vals)
# 11. STACKING AND SPLITTING
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
# Vertical stacking
vertical_stack = np.vstack((A, B))
# Horizontal stacking
horizontal_stack = np.hstack((A, B))
print(vertical_stack)
print(horizontal_stack)
# Splitting
split_arr = np.split(
    np.array([1, 2, 3, 4, 5, 6]),
    3
)
print(split_arr)

