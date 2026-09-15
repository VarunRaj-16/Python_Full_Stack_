print("4. CLASS ATTRIBUTE + INSTANCE ATTRIBUTES")
class Student3:
    collegename = "codegnan"              # Class Attribute
    def __init__(self):
        self.name = "raju"
        self.age = 23
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student3.collegename)
s1 = Student3()
print("Access using object:", s1.collegename)
print("Access using class :", Student3.collegename)
print("5. LOCAL VARIABLE")
class Test:
    def __init__(self):
        x = 10                            # Local variable
        print("Local variable value:", x)
t1 = Test()
# print(x)  → NameError