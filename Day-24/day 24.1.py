print("2. INSTANCE METHOD, CLASS METHOD, STATIC METHOD")
class Demo:
    college = "Codegnan"
    def __init__(self, name):
        self.name = name
    # Instance Method
    def display(self):
        print("Instance Method → Name:", self.name)
    # Class Method
    @classmethod
    def show_college(cls):
        print("Class Method → College:", cls.college)
    # Static Method
    @staticmethod
    def add(a, b):
        return a + b
obj = Demo("Varun")
obj.display()
Demo.show_college()
print("Static Method → Sum:", Demo.add(10, 20))

