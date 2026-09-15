print("3. POSITIONAL ARGUMENTS")
def student_details(name, course):
    print(name, course)
student_details("Ravi", "Python")     # Order matters

print("\n. print() vs return")
def Add_Print(a, b):
    print(a + b)                      # Only displays, returns None
def Add_Return(a, b):
    return a + b                      # Sends value back to caller
result1 = Add_Print(10, 20)
print("Returned value:", result1)     # None
result2 = Add_Return(10, 20)
print("Returned value:", result2)     # 30
