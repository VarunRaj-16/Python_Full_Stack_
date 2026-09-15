print("21. LAMBDA (Anonymous Function)")
square = lambda x: x * x
print("Square of 5:", square(5))

print("\n22. RECURSIVE FUNCTION (Factorial)")
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
