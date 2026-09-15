print("16. break Statement")
numbers = [1, 3, 5, 7, 9, 11]
target = 7
for num in numbers:
    if num == target:
        print("Target found:", num)
        break                    # Exit the loop immediately
print("17. continue Statement") # Print only odd numbers
for num in range(1, 8):
    if num % 2 != 0:
        continue                 # Skip even numbers
    print(num)
print("18. assert Keyword")
x = 10
assert x > 0, "x must be positive"   # Continues if True
print("Assertion passed: x is positive")


