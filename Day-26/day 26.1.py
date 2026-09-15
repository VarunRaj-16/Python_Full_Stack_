print("2. MULTIPLE INHERITANCE")
class Father:
    def dance(self):
        print("dancing")
class Mother:
    def cook(self):
        print("cooking")
class Child(Father, Mother):
    def play(self):
        print("playing")
c = Child()
c.dance()
c.cook()
c.play()
