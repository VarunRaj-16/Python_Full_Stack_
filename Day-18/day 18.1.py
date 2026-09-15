print("3. SUM OF NATURAL NUMBERS USING RECURSION")
def sum_natural(n):
    if n == 1:                    # Base case
        return 1
    else:
        return n + sum_natural(n - 1)
print("Sum of first 5 natural numbers:", sum_natural(5))  # 15
print("4. PASS BY VALUE (Immutable Objects)")
def modify_value(num):
    num += 10                     # Creates a new local variable
    print("Inside function:", num)
x = 5
print("Before function call:", x)
modify_value(x)
print("Outside function:", x)     # Original value remains unchanged
