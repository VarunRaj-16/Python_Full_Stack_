print("9. CALL BY OBJECT REFERENCE - IMMUTABLE")
def change(x):
    x = 100
    print("Inside function:", x)
a = 10
print("Before:", a)
change(a)
print("After:", a)          # Original value remains same
print("10. CALL BY OBJECT REFERENCE - MUTABLE (List)")
def change_list(mylist):
    mylist.append(100)
numbers = [10, 20, 30]
print("Before:", numbers)
change_list(numbers)
print("After:", numbers)    # Original list is modified
