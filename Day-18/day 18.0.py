# DAY 18 - RECURSIVE FUNCTIONS + PASS BY VALUE / REFERENCE
print("1. FACTORIAL USING RECURSION")
def factorial(n):
    if n == 0 or n == 1:          # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case
print("Factorial of 5:", factorial(5))   # 120

print("2. FIBONACCI SERIES USING RECURSION")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print("fibonacci(6):", fibonacci(6))     # 8
print("fibonacci(4):", fibonacci(4))     # 3

