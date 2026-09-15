# DAY 19 - MODULES, BUILT-IN MODULES & FILE/DIRECTORY HANDLING

print("1. IMPORTING MODULES - DIFFERENT WAYS")
import math
print("math.sqrt(25):", math.sqrt(25))
print("math.factorial(5):", math.factorial(5))
print("math.pi:", math.pi)
from math import sqrt, factorial
print("sqrt(16):", sqrt(16))
print("factorial(4):", factorial(4))
import math as m
print("Using alias m.sqrt(36):", m.sqrt(36))

print("2. UNDERSTANDING __name__")
print("Current __name__ value:", __name__)
if __name__ == "__main__":
    print("This file is running directly")
else:
    print("This file is imported as a module")

