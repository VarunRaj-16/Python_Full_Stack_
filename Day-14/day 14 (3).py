print("5. return STOPS THE FUNCTION")
def Demo_Return(a, b):
    c = a + b
    print("Start")
    return c
    print("End")                      # This will never execute
print(Demo_Return(10, 20))

