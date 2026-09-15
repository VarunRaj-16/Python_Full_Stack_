# 17. Largest Digit
def largest_digit(n):
    if n < 10:
        return n
    return max(n % 10, largest_digit(n // 10))
print("Largest digit in 59372:", largest_digit(59372))
# 18. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("7th Fibonacci number:", fibonacci(7))
