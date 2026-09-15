print("5. HYBRID INHERITANCE")
class Person:
    def display(self):
        print("I am a person.")
class Student(Person):
    def show(self):
        print("I am a student.")
class Sports:
    def play(self):
        print("I play sports.")
class CollegeStudent(Student, Sports):
    def college_info(self):
        print("I am a college student.")
cs = CollegeStudent()
cs.display()
cs.show()
cs.play()
cs.college_info()

