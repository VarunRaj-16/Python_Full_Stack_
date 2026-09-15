print("3. METHOD OVERLOADING (Simulated)")
class Greet:
    def hello(self, name=None):
        if name:
            print("Hello", name)
        else:
            print("Hello")
g = Greet()
g.hello()
g.hello("Jani")
print("4. METHOD OVERRIDING")
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.speak()
d.speak()

