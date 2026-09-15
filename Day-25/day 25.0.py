# DAY 25 - POLYMORPHISM IN PYTHON
print("1. DUCK TYPING")
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
def animal_sound(animal):
    animal.speak()
animal_sound(Dog())
animal_sound(Cat())