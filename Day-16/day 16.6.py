print("11. DICTIONARY OPERATIONS")
student = {"name": "Ravi", "age": 22}
print("Access name:", student["name"])
student["age"] = 23                       # Update
print("After update age:", student)
student["course"] = "Python"              # Add new key
print("After adding course:", student)
del student["age"]                        # Remove
print("After deleting age:", student)
print("'name' in student:", "name" in student)
print("'course' not in student:", "course" not in student)


