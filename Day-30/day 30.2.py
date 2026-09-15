print("6. try-except-else-finally")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("Division successful!")
    print("Result is:", result)
finally:
    print("Program has finished execution (with or without errors).")

print("7. Catching Any Exception")
try:
    a = int("hello")
except Exception as e:
    print("Something went wrong:", e)

