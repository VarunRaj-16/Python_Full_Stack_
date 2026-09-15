print("3. INSTANCE ATTRIBUTES USING CONSTRUCTOR")
class Student2:
    def __init__(self):
        self.name = "raju"
        self.age = 23
        print("my name is:", self.name)
        print("my age is:", self.age)
s1 = Student2()
print("Outside → Name:", s1.name)
print("Outside → Age:", s1.age)


