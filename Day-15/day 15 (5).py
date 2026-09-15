# 2. Print numbers from N to 1
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)
print("5 to 1:", end=" ")
print_n_to_1(5)
print()
# 3. Sum of N natural numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)
print("Sum of 1 to 5:", sum_n(5))
# 4. Product of N natural numbers
def product_n(n):
    if n == 1:
        return 1
    return n * product_n(n - 1)
print("Product of 1 to 5:", product_n(5))