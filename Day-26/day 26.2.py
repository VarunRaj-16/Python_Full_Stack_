print("3. MULTILEVEL INHERITANCE")
class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("barking")
class BabyDog(Dog):
    def cry(self):
        print("crying")
b = BabyDog()
b.cry()
b.bark()
b.eat()
