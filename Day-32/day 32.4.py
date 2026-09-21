import numpy as np
# 8. BOOLEAN INDEXING AND FILTERING
arr = np.array([10, 20, 30, 40, 50])
# Boolean indexing
bool_arr = arr > 25
print(bool_arr)
# Filtering
filtered_arr = arr[arr > 25]
print(filtered_arr)
# 9. LINEAR ALGEBRA
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])
# Matrix multiplication
print(np.dot(A, B))
# Determinant
print(np.linalg.det(A))
# Inverse
print(np.linalg.inv(A))
# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)
# Solving linear equations
C = np.array([5, 11])
solution = np.linalg.solve(A, C)
print(solution)

