# DAY 30 - EXCEPTION HANDLING
print("1. BASIC try-except (ZeroDivisionError)")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

print("2. ValueError Example")
try:
    age = int("abc")
    print("Your age is", age)
except ValueError:
    print("Please enter a valid number!")

print("3. IndexError Example")
try:
    nums = [10, 20, 30]
    print(nums[5])
except IndexError:
    print("Index out of range!")


