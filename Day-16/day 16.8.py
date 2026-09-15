print("14. DICTIONARY METHODS – ADDING & UPDATING")
student = {"name": "Ravi"}
student.update({"age": 25, "city": "Hyderabad"})
print("After update():", student)
print("setdefault('course', 'Python'):", student.setdefault("course", "Python"))
print("After setdefault():", student)
print("15. DICTIONARY METHODS – REMOVING")
student = {"name": "Ravi", "age": 22, "course": "Python"}
print("pop('age'):", student.pop("age"))
print("After pop():", student)
print("popitem():", student.popitem())     # Removes last inserted item
print("After popitem():", student)
student.clear()
print("After clear():", student)
