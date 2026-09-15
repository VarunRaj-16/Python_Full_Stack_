print("10. LAMBDA (ANONYMOUS) FUNCTIONS")
greet = lambda: "Welcome to Codegnan"     # No parameters
print(greet())# Square
square = lambda x: x * x
print("Square of 4:", square(4))
add = lambda a, b: a + b       # Addition
print("10 + 20 =", add(10, 20))
largest = lambda a, b: a if a > b else b      # Maximum
print("Largest of 20 and 10:", largest(20, 10))
check = lambda n: "Even" if n % 2 == 0 else "Odd"      # Even or Odd
print("8 is", check(8))
length = lambda text: len(text)      # String length
print("Length of 'Codegnan':", length("Codegnan"))
