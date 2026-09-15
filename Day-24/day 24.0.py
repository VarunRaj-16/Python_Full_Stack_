# DAY 24 - TYPES OF VARIABLES & METHODS + MEMORY CONCEPT
print("1. INSTANCE, CLASS & LOCAL VARIABLES")
class Student:
    college = "ABC College"                 # Class Variable
    def __init__(self, name, age):
        self.name = name                    # Instance Variable
        self.age = age                      # Instance Variable
    def show(self):
        x = 100                             # Local Variable
        print("Local variable x =", x)
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)
s1 = Student("John", 20)
s2 = Student("Alice", 22)
s1.show()
print()
s2.show()

