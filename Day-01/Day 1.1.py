#Basic Statements & Variables
x = 10
print(x)
name = "Varun"
age = 21


#Multiple Assignment
a, b, c = 10, 20, 30
print(a, b, c)
x = y = z = 100


#Reassignment
x = 5
x = 10
print(x)   # Output: 10


#Swapping Variables
a = 10
b = 20
a, b = b, a
print(a, b)   # Output: 20 10



#Deleting Variables
x = 10
del x # print(x) → NameError



#Mutable Object 
numbers = [10, 20]
numbers.append(30)
print(numbers)   # [10, 20, 30]



#Immutable Object 
name = "Python"
name = name + " Programming"
print(name)   # Python Programming
