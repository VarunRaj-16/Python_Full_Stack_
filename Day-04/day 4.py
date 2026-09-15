#SET
#Syntax : set_name = {item1, item2, item3}
student_ids = {101, 102, 103, 104}
print(student_ids)
# Possible Output: {104, 101, 102, 103}   (order may change)

#(Checking Data Type)
student_ids = {101, 102, 103, 104}
print(type(student_ids))
# Output: <class 'set'>

#(Duplicate Values are Automatically Removed)
student_ids = {101, 102, 103, 101}
print(student_ids)
# Output: {101, 102, 103}

#(Empty Set)
# Incorrect (creates a dictionary)
s = {}
print(type(s))          # <class 'dict'>
# Correct way
s = set()
print(s)                # set()
print(type(s))          # <class 'set'>

#Adding an Element
fruits = {"Apple", "Mango"}
fruits.add("Orange")
print(fruits)
# Output: {'Apple', 'Mango', 'Orange'}
