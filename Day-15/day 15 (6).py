# 5. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
# 6. Power Calculation
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
print("2^4 =", power(2, 4))
# 7. Reverse a String
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]
print("Reverse of 'python':", reverse_string("python"))
