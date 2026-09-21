import numpy as np
# 4. SHAPE AND RESHAPING
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Checking shape
print(arr.shape)
# Reshaping
reshaped = arr.reshape(3, 2)
print(reshaped)
# Flattening
flattened = arr.flatten()
print(flattened)
# Transposing
transposed = arr.T
print(transposed)
# 5. ARRAY INDEXING AND SLICING
arr = np.array([10, 20, 30, 40, 50])
# Accessing elements
print(arr[0])
print(arr[-1])
# Slicing
print(arr[1:4])
print(arr[:3])
print(arr[::2])

