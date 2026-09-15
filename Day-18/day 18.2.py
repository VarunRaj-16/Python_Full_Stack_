print("5. PASS BY REFERENCE (Mutable Objects)")
def modify_list(lst):
    lst.append(4)                 # Modifies the original list
numbers = [1, 2, 3]
print("Before function call:", numbers)
modify_list(numbers)
print("After function call:", numbers)   # Original list is modified
print("6. HOW TO PREVENT UNINTENDED MODIFICATIONS")
def modify_list_copy(lst):
    lst = lst[:]                  # Creates a shallow copy
    lst.append(5)
    print("Inside function:", lst)
numbers = [1, 2, 3]
print("Before function call:", numbers)
modify_list_copy(numbers)
print("Outside function:", numbers)      # Original list remains unchanged

