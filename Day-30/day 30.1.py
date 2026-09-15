print("4. Multiple Exceptions")
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero!")

print("5. try-except-else")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered:", num)
    print("No error occurred, so else block runs.")

