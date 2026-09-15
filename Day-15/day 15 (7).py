# 8. Count Characters (without len)
def count_chars(s):
    if s == "":
        return 0
    return 1 + count_chars(s[1:])
print("Character count of 'Python':", count_chars("Python"))

# 12. Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print("Sum of digits of 12345:", sum_of_digits(12345))
# 13. Product of Digits
def product_of_digits(n):
    if n == 0:
        return 1
    return n % 10 * product_of_digits(n // 10)
print("Product of digits of 1234:", product_of_digits(1234))
