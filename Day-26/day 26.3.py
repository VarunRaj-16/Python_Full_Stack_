print("4. HIERARCHICAL INHERITANCE")
class Animal2:
    def eat(self):
        print("eating")
class Dog2(Animal2):
    def bark(self):
        print("dog is barking")
class Cat(Animal2):
    def meow(self):
        print("cat is doing sound like meow")
d = Dog2()
d.bark()
d.eat()
c = Cat()
c.meow()
c.eat()
