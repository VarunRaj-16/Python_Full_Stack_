##Dictionary (dict)
#Accessing Values
student = {
    "name": "Varun",
    "age": 21,
    "city": "Hyd"
}
print(student["name"])   # Varun
print(student["age"])    # 21

#Using get() Method
print(student.get("name"))    # Varun
print(student.get("marks"))   # None  (no error)

##Boolean (bool)
print(10 == 10)   # True
print(10 > 5)     # True
print(10 < 20)    # True
print(10 < 5)     # False

##None (NoneType)
x = None
print(type(x))   # <class 'NoneType'>
employee_name = None
print(employee_name)   # None



