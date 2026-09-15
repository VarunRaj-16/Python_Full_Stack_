print("17. MULTIPLE RETURN VALUES")
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction      # Returns a tuple
x, y = calculate(20, 10)
print("Addition:", x)
print("Subtraction:", y)

print("\n18. FUNCTION CALLING ANOTHER FUNCTION")
def Add_Func(a, b):
    return a + b
def Display():
    result = Add_Func(10, 20)
    print("Result:", result)
Display()
