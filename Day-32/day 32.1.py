import numpy as np
# Identity matrix
identity = np.eye(4)
print(identity)
# Array of a specific value
full_array = np.full((2, 3), 7)
print(full_array)
# 2. GENERATING RANGES
range_arr = np.arange(1, 11, 2)
print(range_arr)
lin_space = np.linspace(0, 100, 5)
print(lin_space)
# 3. RANDOM NUMBER GENERATION
rand_int = np.random.randint(1, 100, (3, 3))
print(rand_int)
rand_float = np.random.rand(3, 3)
print(rand_float)
rand_norm = np.random.randn(3, 3)
print(rand_norm)
rand_choice = np.random.choice([10, 20, 30, 40, 50], 5)
print(rand_choice)
# Setting random seed
np.random.seed(42)
rand_arr = np.random.rand(5)
print(rand_arr)

