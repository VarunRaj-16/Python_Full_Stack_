import numpy as np
# 6. 2D ARRAY SLICING
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix[1, 2])
print(matrix[:, 1])
print(matrix[0:2, 1:3])
# 7. MATHEMATICAL OPERATIONS
arr = np.array([1, 2, 3, 4, 5])
# Element-wise operations
print(arr + 10)
print(arr * 2)
print(arr ** 2)
print(np.sqrt(arr))
# Aggregate functions
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
# Cumulative operations
print(np.cumsum(arr))
print(np.cumprod(arr))

