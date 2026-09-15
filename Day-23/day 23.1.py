print("2. NON-PARAMETERIZED CONSTRUCTOR")
class Student:
    def __init__(self):
        print("I am non parameterized constructor..")
        print("address of self:", id(self))
s1 = Student()
print("address of s1:", id(s1))
s2 = Student()
print("address of s2:", id(s2))
